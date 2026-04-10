# Claude Code 환경 복원 가이드 (새 PC)

이 문서는 cc-sync를 통해 백업된 Claude Code 설정을 새 PC에 복원하는 절차를 설명합니다.

---

## 사전 준비

```bash
# 1. Node.js 설치 (v18 이상)
# https://nodejs.org/ 에서 다운로드

# 2. Claude Code 설치
npm install -g @anthropic-ai/claude-code

# 3. GitHub CLI 설치 및 인증
# https://cli.github.com/ 에서 다운로드
gh auth login

# 4. Claude Code 인증
claude auth
```

---

## 복원 절차

### Step 1. cc-sync 레포 클론

```bash
git clone https://github.com/briankim1027/cc-sync-template.git ~/Project/cc-sync
cd ~/Project/cc-sync
```

### Step 2. 설정 적용 (Git -> ~/.claude/)

```bash
bash apply.sh
```

이 스크립트가 아래 항목들을 `~/.claude/`로 복사합니다:

| 항목 | 설명 |
|------|------|
| `agents/` | 커스텀 에이전트 정의 |
| `hooks/` | 훅 스크립트 |
| `skills/` | 스킬 파일 |
| `commands/` | 슬래시 커맨드 (`/cc-sync`, `/cc-apply` 등) |
| `rules/` | 코딩 스타일, 보안, 테스트 등 규칙 |
| `settings.json` | 글로벌 설정 (MCP 서버, marketplace 등) |
| `CLAUDE.md` | 글로벌 지침 |

### Step 3. Marketplace 등록 및 플러그인 설치

`settings.json`에 marketplace 정보가 포함되어 있으므로, 플러그인만 설치하면 됩니다.

```bash
# marketplace 캐시 업데이트
claude plugin marketplace update

# 핵심 플러그인 설치
claude plugin install oh-my-claudecode
claude plugin install second-claude-code
claude plugin install bkit
claude plugin install consultant
claude plugin install essentials
claude plugin install context-mode
claude plugin install claude-delegator
claude plugin install telegram

# 개발 워크플로우 플러그인
claude plugin install code-simplifier
claude plugin install ralph-loop
claude plugin install git-workflow
claude plugin install security-scanning
claude plugin install testing-suite

# 언어/프레임워크 플러그인
claude plugin install python-development
claude plugin install javascript-typescript
claude plugin install backend-development
claude plugin install nextjs-vercel-pro

# 오케스트레이션 플러그인
claude plugin install agent-orchestration
claude plugin install ai-ml-toolkit
claude plugin install full-stack-orchestration
claude plugin install code-review-ai
claude plugin install performance-optimizer
claude plugin install supabase-toolkit

# 문서/스킬 플러그인
claude plugin install document-skills
claude plugin install example-skills
claude plugin install content

# 기타 플러그인
claude plugin install claude-dashboard
claude plugin install docs-guide
claude plugin install show-me-the-prd
claude plugin install vibe-sunsang
claude plugin install pumasi
claude plugin install last30days
claude plugin install astory-blog-writers
claude plugin install moai-platform-appintoss
claude plugin install ui-ux-pro-max
claude plugin install reflect
claude plugin install ideation
claude plugin install sandbox
claude plugin install workos
claude plugin install developer-experience
claude plugin install pyright-lsp
claude plugin install typescript-lsp
```

> 한 번에 설치하는 스크립트는 아래 [일괄 설치 스크립트](#일괄-설치-스크립트) 참고

### Step 4. 설치 확인

```bash
# 플러그인 상태 확인
claude plugin list

# Claude Code 실행하여 정상 동작 확인
claude
```

---

## 일괄 설치 스크립트

모든 플러그인을 한 번에 설치하려면:

```bash
#!/bin/bash
# install-plugins.sh

PLUGINS=(
  oh-my-claudecode
  second-claude-code
  bkit
  consultant
  essentials
  context-mode
  claude-delegator
  telegram
  code-simplifier
  ralph-loop
  git-workflow
  security-scanning
  testing-suite
  python-development
  javascript-typescript
  backend-development
  nextjs-vercel-pro
  agent-orchestration
  ai-ml-toolkit
  full-stack-orchestration
  code-review-ai
  performance-optimizer
  supabase-toolkit
  document-skills
  example-skills
  content
  claude-dashboard
  docs-guide
  show-me-the-prd
  vibe-sunsang
  pumasi
  last30days
  astory-blog-writers
  moai-platform-appintoss
  ui-ux-pro-max
  reflect
  ideation
  sandbox
  workos
  developer-experience
  pyright-lsp
  typescript-lsp
)

echo "Updating marketplaces..."
claude plugin marketplace update

echo ""
echo "Installing ${#PLUGINS[@]} plugins..."
for plugin in "${PLUGINS[@]}"; do
  echo "Installing $plugin..."
  claude plugin install "$plugin" 2>&1 | tail -1
done

echo ""
echo "Done! Run 'claude plugin list' to verify."
```

사용법:
```bash
chmod +x install-plugins.sh
bash install-plugins.sh
```

---

## Marketplace 목록

`settings.json`에 포함된 marketplace 소스:

| Marketplace | Source |
|-------------|--------|
| anthropic-agent-skills | `anthropics/skills` |
| claude-plugins-official | `anthropics/claude-plugins-official` |
| claude-code-templates | `davila7/claude-code-templates` |
| claude-code-workflows | `wshobson/agents` |
| oh-my-claude-sisyphus | `Yeachan-Heo/oh-my-claudecode` |
| nicknisi | `nicknisi/claude-plugins` |
| bkit-marketplace | `popup-studio-ai/bkit-claude-code` |
| context-mode | `mksglu/context-mode` |
| second-claude-code | `unclejobs-ai/second-claude-code` |
| claude-dashboard | `uppinote20/claude-dashboard` |
| moai-cc-plugins | `modu-ai/cc-plugins` |
| gptaku-plugins | `fivetaku/gptaku_plugins` |
| jarrodwatts-claude-delegator | `jarrodwatts/claude-delegator` |
| ui-ux-pro-max-skill | `nextlevelbuilder/ui-ux-pro-max-skill` |
| open-claude-plugins | `shfc/open-claude-plugins` |
| thedotmack | `thedotmack/claude-mem` |
| last30days-skill | `mvanhorn/last30days-skill` |

marketplace가 누락된 경우 수동 추가:
```bash
claude plugin marketplace add owner/repo
```

---

## 일상적인 동기화

설정 변경 후 백업:
```bash
# Claude Code 내에서
/cc-sync

# 또는 터미널에서
bash ~/Project/cc-sync/sync.sh --auto
```

다른 기기에서 최신 설정 가져오기:
```bash
cd ~/Project/cc-sync
git pull
bash apply.sh
```

---

## 문제 해결

| 증상 | 해결 |
|------|------|
| 플러그인 설치 실패 | `claude plugin marketplace update` 후 재시도 |
| marketplace not found | `claude plugin marketplace add owner/repo`로 수동 추가 |
| 설정 충돌 | `apply.sh`는 덮어쓰기함. 기존 설정 백업 필요시 먼저 `sync.sh` 실행 |
| hooks 동작 안함 | Claude Code 재시작 (`/reload-plugins`) |
