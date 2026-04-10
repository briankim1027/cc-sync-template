# Threads Content Creator (Korea Edition)

Meta Threads 플랫폼에 최적화된 한국어 콘텐츠 생성 Skills입니다.

## 🌟 특징

✨ **Threads 알고리즘 최적화**
- 첫 30분 골든타임 전략
- 참여율 극대화 기법
- 해시태그 전략

🇰🇷 **한국 Threads 문화 반영**
- 자연스러운 한국어 톤
- 공감 중심 콘텐츠
- 인터넷 용어 활용

📈 **높은 참여도**
- 50+ 질문 템플릿
- 30+ CTA 문구
- 5가지 콘텐츠 타입

## 📥 설치 방법

### Personal Skills (개인 사용)

```bash
# 1. Skills 폴더로 이동
cd ~/.claude/skills/

# 2. ZIP 파일 압축 해제
unzip threads-content-creator-kr.zip

# 3. Claude Code 시작
claude
```

### Project Skills (팀 공유)

```bash
# 1. 프로젝트 루트로 이동
cd your-project/

# 2. .claude/skills/ 폴더 생성
mkdir -p .claude/skills/

# 3. ZIP 파일 압축 해제
unzip threads-content-creator-kr.zip -d .claude/skills/

# 4. Git에 커밋
git add .claude/skills/
git commit -m "Add Threads content creator Skill"
git push
```

## 🚀 사용 방법

### 기본 사용

Claude와 대화하면서 Threads 콘텐츠가 필요할 때 자동으로 활성화됩니다.

**예시:**
```
"월요일 출근에 대한 공감 게시글 만들어줘"
"Threads에 올릴 맛집 리뷰 작성해줘"
"재택근무 vs 사무실 출근 투표 게시글 만들어줘"
```

### 상세 옵션 지정

더 구체적인 요청도 가능합니다:

```
주제: 카페 경험
목적: 감성 자극 + 공유 유도
톤: 따뜻하고 감성적
길이: 중간 (200자)
타겟: 20-30대 여성
```

### 템플릿 활용

```bash
# 짧은 게시글
cat templates/short_post.md

# 스토리텔링
cat templates/storytelling.md

# 질문형
cat templates/question.md

# 시리즈
cat templates/series.md

# 트렌드 반응
cat templates/trend.md
```

## 💡 주요 기능

### 1. 알고리즘 최적화
- 첫 문장 Hook 생성
- 이모지 3-5개 자동 배치
- 해시태그 3-5개 전략적 선택
- CTA 자동 삽입

### 2. 한국 톤 적용
- 자연스러운 반말/존댓말
- 인터넷 용어 활용 (ㅋㅋㅋ, ㅠㅠ 등)
- 공감 문구 삽입
- TMI 스타일

### 3. 참여 유도
- 양자택일 질문
- 경험 공유 요청
- 의견 수렴
- 시리즈 구조

### 4. 다양한 포맷
- 단문 (50-100자)
- 중문 (100-300자)
- 장문/스레드 (300자+)
- 질문형
- 스토리텔링

## 🔧 문제 해결

### Q1: Claude가 Skills를 사용하지 않아요

**A:** Description에 맞는 키워드를 사용해보세요.
- "Threads 게시글"
- "소셜 미디어 콘텐츠"
- "참여 유도 게시글"

### Q2: 톤이 어색해요

**A:** KOREAN_THREADS_GUIDE.md를 참조하여 원하는 톤을 명시하세요.
- "친근한 반말 톤으로"
- "전문적이지만 따뜻하게"
- "유머러스하게"

### Q3: 게시글이 너무 길어요

**A:** 길이를 명시하세요.
- "짧은 게시글 (100자 이내)"
- "중간 길이 (200자)"

### Q4: 해시태그가 맘에 안 들어요

**A:** 원하는 해시태그를 직접 지정하세요.
- "해시태그는 #직장인 #워라밸 #팁 사용"

## 📚 포함된 리소스

1. **SKILL.md** - 메인 지침 파일
2. **REFERENCE.md** - Threads 알고리즘 심층 분석
3. **KOREAN_THREADS_GUIDE.md** - 한국 Threads 문화 가이드
4. **ENGAGEMENT_TACTICS.md** - 참여 유도 전략 50+
5. **templates/** - 5가지 콘텐츠 템플릿

## 📊 업데이트 이력

**v1.0.0 (2025-12-24)**
- 초기 릴리즈
- Threads 알고리즘 최적화
- 한국 Threads 문화 반영
- 50+ 참여 유도 전략
- 5가지 템플릿 제공

## 📝 라이선스

MIT License

## 🤝 피드백

개선 사항이나 버그 리포트는 이슈로 남겨주세요!

---

Made with ❤️ for Korean Threads Creators
