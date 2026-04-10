---
description: Safely clear context by creating HANDOFF.md first
---

# /safe-clear - Safe Context Clear

> **목적**: HANDOFF.md를 자동 생성한 후 안전하게 컨텍스트 초기화

---

## 🎯 명령어 동작

이 명령어는 다음을 자동으로 수행합니다:

1. **현재 세션 분석** - 완료/진행/다음 작업 파악
2. **HANDOFF.md 자동 생성** - 템플릿 기반으로 작성
3. **사용자 확인 요청** - HANDOFF.md 검토
4. **컨텍스트 초기화** - `/clear` 실행

---

## 📋 실행 단계

### Step 1: 세션 상태 분석

다음 정보를 자동으로 수집합니다:

- 현재 토큰 사용량
- 최근 수정된 파일
- 진행 중인 작업
- Git 커밋 히스토리 (최근 5개)

---

### Step 2: HANDOFF.md 생성

프로젝트 루트에 `HANDOFF.md` 파일을 생성합니다:

```markdown
# HANDOFF.md

## 📅 세션 정보

- 이전 세션 종료: [자동 생성 시각]
- 토큰 사용량: [현재 토큰] / 200k
- 작업 진행률: [추정치]%

## ✅ 완료된 작업

[Git 커밋 히스토리 기반으로 자동 생성]

## 🚧 진행 중인 작업

[현재 열린 파일 및 최근 수정 파일 기반]

## 📝 다음 단계

[사용자가 직접 작성 필요]

## ⚠️ 주의사항

[중요한 이슈나 결정사항]
```

---

### Step 3: 사용자 확인

생성된 HANDOFF.md를 표시하고:

```
✅ HANDOFF.md가 생성되었습니다.

📄 내용 확인:
[HANDOFF.md 내용 표시]

❓ 이대로 진행하시겠습니까?

1. ✅ Yes - /clear 실행
2. ✏️ Edit - HANDOFF.md 수정 후 진행
3. ❌ Cancel - 취소
```

---

### Step 4: 컨텍스트 초기화

사용자 확인 후 `/clear` 명령 실행

---

## 💡 사용 방법

### 기본 사용

```
/safe-clear
```

단순히 명령어만 입력하면 자동으로 모든 단계 실행

---

### 추가 정보 제공 (선택적)

```
/safe-clear
다음 단계: 사용자 프로필 페이지 구현
주의사항: DB 스키마 변경 계획 중
```

추가 정보를 제공하면 HANDOFF.md에 자동으로 포함

---

## 🔧 구현 로직

### 1. 토큰 사용량 확인

```typescript
// 현재 토큰 사용량 확인
const currentTokens = getCurrentTokenUsage();
const percentage = (currentTokens / 200000) * 100;

console.log(
  `현재: ${currentTokens.toLocaleString()} / 200,000 (${percentage.toFixed(1)}%)`,
);
```

---

### 2. 최근 작업 수집

```bash
# Git 커밋 히스토리 (최근 5개)
git log -5 --oneline --decorate

# 최근 수정된 파일
git status --short

# 현재 브랜치
git branch --show-current
```

---

### 3. HANDOFF.md 템플릿 채우기

```typescript
const handoffContent = `
# HANDOFF.md

## 📅 세션 정보
- 이전 세션 종료: ${new Date().toISOString()}
- 토큰 사용량: ${currentTokens.toLocaleString()} / 200k
- 작업 진행률: ${estimatedProgress}%

## ✅ 완료된 작업
${gitCommits.map((c) => `- ${c}`).join("\n")}

## 🚧 진행 중인 작업
${modifiedFiles.map((f) => `- ${f.status} ${f.path}`).join("\n")}

## 📝 다음 단계
${userProvidedNext || "[ ] 작업 계획 업데이트 필요"}

## ⚠️ 주의사항
${userProvidedWarnings || "없음"}
`;
```

---

### 4. 파일 생성 및 확인

```typescript
// HANDOFF.md 생성
await writeFile("./HANDOFF.md", handoffContent);

// 사용자에게 확인 요청
const confirmation = await askUser(
  "HANDOFF.md가 생성되었습니다. /clear를 진행하시겠습니까?",
  ["Yes", "Edit", "Cancel"],
);

if (confirmation === "Yes") {
  // /clear 실행
  await executeClear();
}
```

---

## 🎯 예상 워크플로우

### 사용자 입력

```
/safe-clear
```

---

### Agent 응답

```
🔍 세션 상태 분석 중...

📊 현재 상태:
- 토큰: 85,432 / 200,000 (42.7%)
- 브랜치: feature/user-auth
- 수정된 파일: 8개

✅ 최근 완료된 작업 (Git 커밋):
1. feat: JWT 인증 구현
2. test: 로그인 테스트 추가
3. refactor: 에러 핸들링 개선
4. fix: 토큰 만료 버그 수정
5. docs: API 문서 업데이트

🚧 진행 중인 작업:
- src/app/login/page.tsx (수정됨)
- src/hooks/useAuth.ts (수정됨)
- tests/auth/login.test.tsx (추가됨)

📄 HANDOFF.md 생성 완료!

─────────────────────────────────────
# HANDOFF.md 미리보기

## 📅 세션 정보
- 이전 세션 종료: 2026-01-23T14:54:35+09:00
- 토큰 사용량: 85,432 / 200k
- 작업 진행률: 70%

## ✅ 완료된 작업
- feat: JWT 인증 구현
- test: 로그인 테스트 추가
- refactor: 에러 핸들링 개선
- fix: 토큰 만료 버그 수정
- docs: API 문서 업데이트

## 🚧 진행 중인 작업
- M src/app/login/page.tsx
- M src/hooks/useAuth.ts
- A tests/auth/login.test.tsx

## 📝 다음 단계
[ ] 작업 계획 업데이트 필요

## ⚠️ 주의사항
없음
─────────────────────────────────────

❓ 다음 단계를 선택하세요:
1. ✅ 이대로 /clear 실행
2. ✏️ HANDOFF.md 수정 후 /clear
3. ❌ 취소 (HANDOFF.md만 생성)
```

---

### 사용자 선택: 2 (수정)

```
다음 단계 추가:
- 회원가입 페이지 구현
- 비밀번호 재설정 기능

주의사항 추가:
- Refresh token 관리 방법 결정 필요
```

---

### Agent 최종 확인

```
✅ HANDOFF.md 업데이트 완료!

## 📝 다음 단계
- [ ] 회원가입 페이지 구현
- [ ] 비밀번호 재설정 기능

## ⚠️ 주의사항
- Refresh token 관리 방법 결정 필요

🔄 /clear를 실행합니다...

✨ 컨텍스트가 초기화되었습니다!

💡 다음 세션 시작 시:
"HANDOFF.md 읽어줘" 라고 말씀해주세요.
```

---

## ⚠️ 주의사항

### 파일 덮어쓰기

기존 HANDOFF.md가 있으면:

```
⚠️ HANDOFF.md가 이미 존재합니다.

1. 📝 병합 - 기존 내용 유지하고 새 세션 추가
2. 🔄 덮어쓰기 - 새로 생성
3. ❌ 취소
```

---

### Git 미커밋 변경사항

```
⚠️ 커밋되지 않은 변경사항이 있습니다:

수정됨:
- src/app/login/page.tsx
- src/hooks/useAuth.ts

권장: 먼저 커밋한 후 /safe-clear를 실행하세요.

계속 진행하시겠습니까? (y/N)
```

---

## 🎯 /clear vs /safe-clear

### /clear (기본)

```
❌ 위험:
- HANDOFF.md 없으면 컨텍스트 손실
- 수동으로 준비 필요

사용 시점:
- HANDOFF.md가 이미 준비됨
```

---

### /safe-clear (안전)

```
✅ 안전:
- 자동으로 HANDOFF.md 생성
- 확인 단계 포함
- Git 상태 체크

사용 시점:
- 대부분의 경우 (권장)
```

---

## 💡 프로 팁

### Tip 1: 정기적 사용

```
토큰 80k 도달 시:
→ /safe-clear 습관화
→ 항상 안전한 리셋
```

---

### Tip 2: 추가 정보 미리 준비

VS Code 메모장에 적어두고:

```
다음 단계:
- 회원가입 구현
- 이메일 인증

주의사항:
- DB 스키마 변경 예정
```

복사해서 `/safe-clear` 후 붙여넣기

---

### Tip 3: Git과 연동

```bash
# /safe-clear 전에
git add .
git commit -m "WIP: 로그인 진행 중"

# 그 후 /safe-clear
→ 깔끔한 Git 히스토리
```

---

## 🔄 다른 Commands와 연계

### /checkpoint (선택적)

```
/checkpoint before-clear
→ 현재 상태 스냅샷 저장

/safe-clear
→ HANDOFF.md + /clear

새 세션:
→ HANDOFF.md 읽기
→ 작업 재개
```

---

## 📊 예상 효과

**Before (/clear 직접 사용)**:

- HANDOFF.md 수동 작성: 5분
- 실수로 건너뛰기: 종종 발생
- 컨텍스트 손실: 1시간 재설명

**After (/safe-clear 사용)**:

- 자동 생성: 0분
- 강제 확인: 실수 방지
- 컨텍스트 유지: 즉시 재개

**절약**: 시간 + 정신적 안정감

---

## ✅ 요약

**/safe-clear = 걱정 없는 컨텍스트 리셋**

1. 자동 분석
2. HANDOFF.md 생성
3. 사용자 확인
4. 안전한 /clear

**권장**: 이제부터 `/clear` 대신 **항상 `/safe-clear`** 사용! 🎯
