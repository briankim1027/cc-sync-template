#!/bin/bash
set -e

# Skill activation hook - analyzes user prompts and suggests relevant skills
# Based on skill-rules.json configuration
# Runs on UserPromptSubmit event

# Read input from stdin
input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt // empty' | tr '[:upper:]' '[:lower:]')

# Exit if no prompt
if [[ -z "$prompt" ]]; then
    exit 0
fi

# Find skill-rules.json
rules_file=""
if [[ -n "$CLAUDE_PROJECT_DIR" ]] && [[ -f "$CLAUDE_PROJECT_DIR/.claude/skills/skill-rules.json" ]]; then
    rules_file="$CLAUDE_PROJECT_DIR/.claude/skills/skill-rules.json"
elif [[ -f "$HOME/.claude/skills/skill-rules.json" ]]; then
    rules_file="$HOME/.claude/skills/skill-rules.json"
fi

# Exit if no rules file
if [[ -z "$rules_file" ]]; then
    exit 0
fi

# Extract skill names
skill_names=$(jq -r '.skills | keys[]' "$rules_file" 2>/dev/null)

if [[ -z "$skill_names" ]]; then
    exit 0
fi

matched_critical=""
matched_high=""
matched_medium=""
matched_low=""

# Check each skill
while IFS= read -r skill_name; do
    matched=false
    priority=$(jq -r ".skills[\"$skill_name\"].priority // \"medium\"" "$rules_file")

    # Check keywords
    keywords=$(jq -r ".skills[\"$skill_name\"].promptTriggers.keywords[]? // empty" "$rules_file" 2>/dev/null)
    while IFS= read -r keyword; do
        if [[ -n "$keyword" ]] && echo "$prompt" | grep -qi "$keyword" 2>/dev/null; then
            matched=true
            break
        fi
    done <<< "$keywords"

    # Check intent patterns if not matched by keyword
    if [[ "$matched" != "true" ]]; then
        patterns=$(jq -r ".skills[\"$skill_name\"].promptTriggers.intentPatterns[]? // empty" "$rules_file" 2>/dev/null)
        while IFS= read -r pattern; do
            if [[ -n "$pattern" ]] && echo "$prompt" | grep -qiE "$pattern" 2>/dev/null; then
                matched=true
                break
            fi
        done <<< "$patterns"
    fi

    # Add to matched list by priority
    if [[ "$matched" == "true" ]]; then
        case "$priority" in
            critical) matched_critical="${matched_critical}  → ${skill_name}\n" ;;
            high)     matched_high="${matched_high}  → ${skill_name}\n" ;;
            medium)   matched_medium="${matched_medium}  → ${skill_name}\n" ;;
            low)      matched_low="${matched_low}  → ${skill_name}\n" ;;
        esac
    fi
done <<< "$skill_names"

# Generate output if matches found
if [[ -n "$matched_critical" || -n "$matched_high" || -n "$matched_medium" || -n "$matched_low" ]]; then
    output="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    output+="SKILL ACTIVATION CHECK\n"
    output+="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

    if [[ -n "$matched_critical" ]]; then
        output+="CRITICAL SKILLS (REQUIRED):\n${matched_critical}\n"
    fi
    if [[ -n "$matched_high" ]]; then
        output+="RECOMMENDED SKILLS:\n${matched_high}\n"
    fi
    if [[ -n "$matched_medium" ]]; then
        output+="SUGGESTED SKILLS:\n${matched_medium}\n"
    fi
    if [[ -n "$matched_low" ]]; then
        output+="OPTIONAL SKILLS:\n${matched_low}\n"
    fi

    output+="ACTION: Consider using Skill tool for matched skills\n"
    output+="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

    echo -e "$output"
fi

exit 0
