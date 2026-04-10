# Session Learn Skill

세션에서 발생한 실수, 교훈, 패턴을 분석하고 `~/.claude/LEARNINGS.md`에 자동으로 기록합니다.

## Trigger
- `/session-learn` 명령어 실행
- 세션 종료 전 학습사항 정리 요청

## Process

### Step 1: 세션 분석
현재 세션에서 발생한 다음 항목들을 분석합니다:

1. **실수/에러**: 발생한 문제와 원인
2. **해결 패턴**: 문제 해결에 사용된 방법
3. **새로운 발견**: 프로젝트/도구에 대한 새로운 정보
4. **개선점**: 다음에 더 잘할 수 있는 방법

### Step 2: 분류 및 심각도 평가

**심각도 분류**:
- 🔴 **Critical**: 데이터 손실, 보안 위험, 프로덕션 장애 가능성
- 🟡 **Pattern**: 반복 발생 가능, 효율성 저하
- 🟢 **Tip**: 알면 좋은 정보, 효율성 향상

**카테고리**:
- `git`: 버전 관리 관련
- `env`: 환경/설정 관련
- `code`: 코딩 패턴/실수
- `tool`: 도구 사용법
- `workflow`: 작업 흐름
- `project`: 프로젝트 특화

### Step 3: LEARNINGS.md 업데이트

분석된 교훈을 `~/.claude/LEARNINGS.md`에 추가합니다.

**추가 형식**:
```markdown
## [심각도] [카테고리] 제목
- **날짜**: YYYY-MM-DD
- **프로젝트**: 프로젝트명
- **상황**: 무엇이 발생했는가
- **원인**: 왜 발생했는가
- **교훈**: 다음에 어떻게 해야 하는가
```

### Step 4: 중복 검사 및 통합

1. 기존 LEARNINGS.md 읽기
2. 유사한 교훈이 있는지 확인
3. 중복 시: 기존 항목에 사례 추가
4. 신규 시: 새 항목 추가

### Step 5: 요약 보고

사용자에게 다음을 보고합니다:
- 추가된 교훈 수
- 카테고리별 분류
- 주요 교훈 요약

## Output Format

```markdown
# 📚 Session Learning Report

## 분석 결과
- **세션 기간**: [시작] ~ [종료]
- **프로젝트**: [프로젝트명]
- **발견된 교훈**: N개

## 추가된 교훈

### 🔴 Critical
- [교훈 제목]: [간단 설명]

### 🟡 Pattern
- [교훈 제목]: [간단 설명]

### 🟢 Tip
- [교훈 제목]: [간단 설명]

## LEARNINGS.md 업데이트 완료 ✅
경로: ~/.claude/LEARNINGS.md
```

## Integration

이 스킬은 다음과 통합됩니다:
- `~/.claude/LEARNINGS.md`: 교훈 저장소
- `~/.claude/CLAUDE.md`: LEARNINGS.md 참조
- `/reflect` 스킬: 세션 분석과 연계

## Usage Examples

```bash
# 기본 사용
/session-learn

# 특정 카테고리만 분석
/session-learn --category git

# 프로젝트 명시
/session-learn --project cc-mirror

# 강제 추가 (중복 검사 스킵)
/session-learn --force
```

## Auto-Prompt (권장)

세션 종료 시 자동으로 물어보기:
```
"이번 세션에서 LEARNINGS.md에 추가할 교훈이 있나요? /session-learn을 실행할까요?"
```

## Maintenance

### 정기 정리 (월 1회 권장)
```bash
/session-learn --cleanup
```
- 30일 이상 된 🟢 Tip 항목 검토
- 중복 항목 통합
- 더 이상 유효하지 않은 항목 제거

### 통계 확인
```bash
/session-learn --stats
```
- 카테고리별 교훈 수
- 가장 많이 발생하는 실수 유형
- 시간대별 트렌드
