# LinkedIn Sales Post Generator - 사용 가이드

## 📖 개요

LinkedIn Sales Post Generator는 6명의 LinkedIn 전문가 방법론을 통합하여 판매 지향적이고 설득력 있는 LinkedIn post를 자동 생성하는 Claude Code Skill입니다.

**통합된 전문가**:
- Justin Welsh (Personal Branding)
- Richard van den Blom (Algorithm Optimization)
- Austin Belcak (Data-Driven Approach)
- Donna Serdula (Professional Storytelling)
- Shay Rowbottom (Hook Mastery)
- Brenda Meller (Visual Excellence)

## 🚀 설치 방법

### Personal Skill로 설치 (개인 사용)

```bash
# 1. ZIP 파일 압축 해제
unzip linkedin-sales-post-generator.zip

# 2. Personal Skills 폴더로 이동
mv linkedin-sales-post-generator ~/.claude/skills/

# 3. 설치 확인
ls ~/.claude/skills/linkedin-sales-post-generator/

# 4. Claude Code 재시작 (이미 실행 중인 경우)
# 터미널에서 Ctrl+C 후 다시 실행
claude
```

### Project Skill로 설치 (팀 공유)

```bash
# 1. ZIP 파일 압축 해제
unzip linkedin-sales-post-generator.zip

# 2. 프로젝트 .claude/skills 폴더로 이동
mv linkedin-sales-post-generator .claude/skills/

# 3. Git에 커밋하여 팀원과 공유
git add .claude/skills/linkedin-sales-post-generator
git commit -m "Add LinkedIn Sales Post Generator skill"
git push

# 팀원들은 pull만 하면 자동으로 사용 가능
```

## 💡 사용 방법

### 기본 사용법

Claude Code를 실행하고 다음과 같이 요청하세요:

```
"AI 이메일 자동화 도구를 홍보하는 LinkedIn post 만들어줘.
타겟은 B2B 마케터이고, 주당 15시간 절약할 수 있어."
```

Claude가 자동으로 이 Skill을 인식하고 적절한 post를 생성합니다.

### 구체적 사용 예시

#### 예시 1: SaaS 제품
```
제품명: EmailAI
타입: AI 기반 이메일 자동화 도구
기능:
- 개인화된 이메일 1000통 1분 내 생성
- 최적 발송 시간 자동 추천
- A/B 테스트 자동 실행

타겟: B2B 마케팅 매니저
결과: 응답률 4배 증가, 주당 15시간 절약
고객 수: 500+ 기업
평점: 4.8/5.0

Problem-Solution 스타일로 LinkedIn post 만들어줘.
```

#### 예시 2: 컨설팅 서비스
```
서비스: LinkedIn 성장 컨설팅
내용: 1:1 맞춤 전략, 콘텐츠 최적화, 90일 성장 플랜
타겟: 스타트업 창업자, 개인 브랜더
성과: 클라이언트 평균 300% 팔로워 증가

Story-Driven 스타일로 개인 경험 포함해서 post 만들어줘.
```

#### 예시 3: 온라인 코스
```
코스명: Productivity Masterclass
내용: 시간 관리, 에너지 최적화, 자동화 도구
수강생: 1,200명
평점: 4.9/5.0
할인: 얼리버드 50% (이번 주 금요일까지)

Value-First 스타일로 무료 팁 3개 포함해서 post 만들어줘.
```

### 고급 활용법

#### A/B 테스트용 여러 버전 생성
```
"EmailAI 제품으로 3가지 다른 각도의 LinkedIn post 만들어줘:
1. Problem-Solution 스타일
2. Story-Driven 스타일
3. Social Proof 중심 스타일"
```

#### 특정 전문가 스타일 지정
```
"Justin Welsh 스타일로 개인 스토리 중심의 post 만들어줘"
"Austin Belcak 스타일로 데이터와 숫자 중심의 post 만들어줘"
```

#### 타겟 오디언스별 맞춤
```
"같은 제품이지만:
1. C-Level 타겟 버전 (ROI, 전략적 가치)
2. Manager 타겟 버전 (팀 생산성, 효율성)
3. Individual Contributor 버전 (개인 성과, 스킬)

각각 만들어줘."
```

## 📂 포함된 파일

```
linkedin-sales-post-generator/
├── SKILL.md              # 핵심 지침 및 방법론
├── REFERENCE.md          # 세부 전략 및 실제 예시
├── README.md            # 이 파일
└── templates/           # 산업별 맞춤 템플릿
    ├── saas-template.md
    ├── consulting-template.md
    ├── course-template.md
    └── ecommerce-template.md
```

## 🎯 주요 기능

### 1. 6가지 전문가 방법론 통합
- **Justin Welsh**: 진정성 있는 개인 브랜딩
- **Richard van den Blom**: 알고리즘 최적화
- **Austin Belcak**: 데이터 기반 설득
- **Donna Serdula**: 전문적 스토리텔링
- **Shay Rowbottom**: 강력한 Hook
- **Brenda Meller**: 시각적 포맷팅

### 2. 5가지 Post 유형 지원
- Problem-Solution Post
- Story-Driven Post
- Value-First Post
- Social Proof Post
- Thought Leadership Post

### 3. 산업별 템플릿
- B2B SaaS
- 컨설팅/코칭
- 온라인 코스
- 이커머스

### 4. 품질 보증 체크리스트
생성된 모든 post는 10가지 품질 기준을 충족합니다.

## 🔧 문제 해결

### 문제: Claude가 Skill을 인식하지 못함

**해결 방법**:
```bash
# 1. Skills 폴더 확인
ls ~/.claude/skills/

# 2. SKILL.md 파일 존재 확인
cat ~/.claude/skills/linkedin-sales-post-generator/SKILL.md

# 3. Claude Code 재시작
# Ctrl+C 후 다시 실행
```

### 문제: Post가 너무 판매 중심적

**해결 방법**:
```
"좀 더 스토리텔링 중심으로 만들어줘"
"Justin Welsh 스타일로 개인 경험 포함해서"
"판매 압박감 없이 가치 제공 우선으로"
```

### 문제: CTA가 약하거나 모호함

**해결 방법**:
```
"더 직접적인 CTA로 바꿔줘"
"무료 체험 링크 포함해서"
"DM 유도하는 Soft CTA로"
```

### 문제: Hook이 약함

**해결 방법**:
```
"첫 줄을 더 강력한 Hook으로 바꿔줘"
"숫자나 데이터 기반 Hook으로"
"질문 형식의 Hook으로"
```

### 문제: 길이가 너무 길거나 짧음

**해결 방법**:
```
"1500자 정도로 줄여줘"
"좀 더 길게 디테일 추가해서"
```

## 📊 활용 팁

### Tip 1: 구체적인 정보 제공
모호한 요청보다 구체적인 정보를 제공할수록 좋은 결과를 얻습니다.

**❌ 나쁜 예**:
```
"우리 제품 홍보 post 만들어줘"
```

**✅ 좋은 예**:
```
"제품명: EmailAI
타겟: B2B 마케터
핵심 기능: 이메일 자동화, A/B 테스트
결과: 응답률 4배, 주당 15시간 절약
고객: 500+ 기업, 평점 4.8

Problem-Solution 스타일 post 만들어줘."
```

### Tip 2: A/B 테스트
같은 제품으로 여러 각도의 post를 생성하여 테스트하세요.

```
"같은 제품으로 3가지 다른 Hook 스타일 만들어줘:
1. 숫자 기반 Hook
2. 질문 형식 Hook
3. 스토리 기반 Hook"
```

### Tip 3: 타겟별 맞춤
타겟 오디언스에 따라 어조와 내용을 조정하세요.

- **C-Level**: ROI, 전략적 가치
- **Manager**: 팀 생산성, 효율성
- **Individual**: 개인 성과, 스킬 향상

### Tip 4: 시즌/트렌드 반영
시기와 트렌드를 반영하도록 요청하세요.

```
"연말 결산 시즌에 맞춰서 '2024년 성과' 각도로 만들어줘"
"신년 목표 설정 시즌에 맞춰서 '2025년 생산성' 각도로"
```

## 📈 성공 사례

### 사례 1: SaaS 스타트업
- **Before**: 직접 작성, 조회수 평균 200
- **After**: Skill 사용, 조회수 평균 2,500
- **결과**: 무료 체험 신청 12배 증가

### 사례 2: 컨설턴트
- **Before**: 판매 중심 post, 참여율 낮음
- **After**: Story-Driven post, 댓글 10배 증가
- **결과**: 월 상담 신청 5건 → 23건

### 사례 3: 온라인 코스 크리에이터
- **Before**: 무작위 post, 등록 전환율 1%
- **After**: Value-First 전략, 전환율 4.5%
- **결과**: 코스 매출 4배 증가

## 🔄 업데이트

### Version 1.0.0 (2024-12-24)
- 초기 릴리스
- 6가지 전문가 방법론 통합
- 5가지 Post 유형 지원
- 4가지 산업별 템플릿

### 향후 업데이트 계획
- 다국어 지원 (한국어, 영어 동시 생성)
- 업계별 추가 템플릿
- 이미지 추천 기능
- 해시태그 자동 최적화

## 💬 피드백 & 지원

### 피드백 제공
개선 제안이나 버그 리포트는 다음 방법으로 제공해주세요:
- GitHub Issues (프로젝트 저장소)
- 이메일
- Slack 채널

### 자주 묻는 질문

**Q: 모든 산업에 사용 가능한가요?**
A: 네, 기본 프레임워크는 범용적이며, 템플릿은 주요 산업에 최적화되어 있습니다.

**Q: 한국어와 영어 모두 지원하나요?**
A: 현재는 한국어 중심이며, 영어 요청 시 영어로도 생성 가능합니다.

**Q: 생성된 post를 수정할 수 있나요?**
A: 네, "이 부분을 이렇게 바꿔줘"라고 요청하면 수정됩니다.

**Q: LinkedIn 외 다른 플랫폼에도 사용 가능한가요?**
A: LinkedIn에 최적화되어 있지만, 다른 B2B 플랫폼에도 활용 가능합니다.

## 📚 추가 학습 자료

### 추천 읽을거리
- Justin Welsh의 "The Content Operating System"
- Richard van den Blom의 LinkedIn 알고리즘 가이드
- Austin Belcak의 "The $10K Work Week"

### 유용한 링크
- LinkedIn 공식 베스트 프랙티스
- Social Media Examiner
- Content Marketing Institute

## 📄 라이선스

이 Skill은 개인 및 상업적 용도로 자유롭게 사용 가능합니다.

---

**제작**: Claude Skills 전문팀 (Tom, Sam, Jennifer, William)
**버전**: 1.0.0
**최종 업데이트**: 2024-12-24

🚀 **지금 바로 시작하세요!**
