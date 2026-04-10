#!/bin/bash
set -e

# Post-tool-use hook that tracks edited files and their project context
# Runs after Edit, MultiEdit, or Write tools complete successfully
# Enables Stop hooks to selectively build/typecheck only changed projects

# Read tool information from stdin
tool_info=$(cat)

# Extract relevant data
tool_name=$(echo "$tool_info" | jq -r '.tool_name // empty')
file_path=$(echo "$tool_info" | jq -r '.tool_input.file_path // empty')
session_id=$(echo "$tool_info" | jq -r '.session_id // empty')

# Skip if not an edit tool or no file path
if [[ ! "$tool_name" =~ ^(Edit|MultiEdit|Write)$ ]] || [[ -z "$file_path" ]]; then
    exit 0
fi

# Skip markdown and config files
if [[ "$file_path" =~ \.(md|markdown|json|yaml|yml|toml)$ ]]; then
    exit 0
fi

# Determine project dir - use CLAUDE_PROJECT_DIR or fallback
project_dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"

# Create cache directory
cache_dir="$project_dir/.claude/tsc-cache/${session_id:-default}"
mkdir -p "$cache_dir"

# Detect project/service from file path
detect_project() {
    local file="$1"
    local root="$project_dir"

    # Remove project root from path
    local relative_path="${file#$root/}"
    # Handle Windows paths
    relative_path="${relative_path#$root\\}"

    # Extract first directory component
    local project=$(echo "$relative_path" | sed 's|[/\\].*||')

    case "$project" in
        frontend|client|web|app|ui|src|backend|server|api|services|packages|libs|apps)
            echo "$project"
            ;;
        *)
            if [[ ! "$relative_path" =~ [/\\] ]]; then
                echo "root"
            else
                echo "$project"
            fi
            ;;
    esac
}

# Detect build/tsc commands for a project
get_tsc_command() {
    local project="$1"
    local project_path="$project_dir/$project"

    if [[ -f "$project_path/tsconfig.json" ]]; then
        if [[ -f "$project_path/tsconfig.app.json" ]]; then
            echo "cd \"$project_path\" && npx tsc --project tsconfig.app.json --noEmit"
        else
            echo "cd \"$project_path\" && npx tsc --noEmit"
        fi
    elif [[ -f "$project_dir/tsconfig.json" ]] && [[ "$project" == "root" || "$project" == "src" ]]; then
        echo "cd \"$project_dir\" && npx tsc --noEmit"
    fi
}

# Detect project
project=$(detect_project "$file_path")

# Skip if unknown
if [[ -z "$project" ]]; then
    exit 0
fi

# Log edited file with timestamp
echo "$(date +%s):$file_path:$project" >> "$cache_dir/edited-files.log"

# Track affected projects (deduplicated)
if ! grep -q "^$project$" "$cache_dir/affected-projects.txt" 2>/dev/null; then
    echo "$project" >> "$cache_dir/affected-projects.txt"
fi

# Store tsc command for affected project
tsc_cmd=$(get_tsc_command "$project")
if [[ -n "$tsc_cmd" ]]; then
    # Use temp file + sort for dedup
    echo "$project:tsc:$tsc_cmd" >> "$cache_dir/commands.txt.tmp"
    sort -u "$cache_dir/commands.txt.tmp" > "$cache_dir/commands.txt" 2>/dev/null
    rm -f "$cache_dir/commands.txt.tmp"
fi

exit 0
