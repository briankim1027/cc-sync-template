# YouTube Workflow 사용 가이드

## 개요

YouTube Workflow는 YouTube 영상 URL만 입력하면 자동으로 정보 수집, 자막 추출, 학습용 요약 프롬프트 생성, 이메일 전송까지 완료하는 통합 자동화 스킬입니다.

## 워크플로우 단계

```
1. YouTube URL 입력
   ↓
2. 비디오 정보 수집 (youtube-info)
   - 제목, 채널, 재생시간
   - 조회수, 좋아요, 설명
   ↓
3. 자막 추출 (youtube-captions)
   - 전체 자막 텍스트
   - 타임스탬프 구간
   ↓
4. 요약 프롬프트 생성 (youtube-summary)
   - 학습용 템플릿 적용
   - Claude용 프롬프트 생성
   ↓
5. 파일 저장
   - JSON 데이터
   - Markdown 프롬프트
   - HTML 이메일 초안
   ↓
6. 이메일 전송 (선택)
   - Gmail SMTP
   - 첨부파일 포함
```

## 설치 및 설정

### 1. 필수 스킬 확인

다음 3개 스킬이 설치되어 있어야 합니다:
- `youtube-info` (C:\Users\c\.claude\skills\youtube-info\)
- `youtube-captions` (C:\Users\c\.claude\skills\youtube-captions\)
- `youtube-summary` (C:\Users\c\.claude\skills\youtube-summary\)

### 2. API 키 준비

`.env` 파일 또는 환경 변수에 다음 키들을 설정:

```env
YOUTUBE_API_KEY=AIzaSy...
APIFY_API_KEY=apify_api_...
EMAIL_RECIPIENTS=user1@example.com,user2@example.com
```

### 3. Gmail 설정 (이메일 전송용, 선택사항)

Gmail에서 App Password 생성:
1. https://myaccount.google.com/apppasswords 방문
2. "Mail" 선택, "Other (Custom name)" 선택
3. "YouTube Workflow" 입력
4. 생성된 16자리 비밀번호 복사
5. `.env`에 추가:

```env
GMAIL_SENDER=your_email@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
```

## 사용 방법

### 방법 1: 직접 실행 (권장)

```bash
python scripts/run_youtube_workflow.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  "YOUTUBE_API_KEY" \
  "APIFY_API_KEY" \
  "recipient@example.com" \
  --output "./output"
```

### 방법 2: .env 파일 사용 (간편)

```bash
python scripts/run_workflow_from_env.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  ".env"
```

### 방법 3: Claude에게 요청

```
이 YouTube 영상을 요약해주세요:
https://www.youtube.com/watch?v=VIDEO_ID

youtube-workflow 스킬을 사용해서 자동으로 처리해주세요.
```

## 출력 파일

워크플로우는 다음 파일들을 생성합니다:

### 1. 데이터 파일 (JSON)
- **파일명**: `{video_title}_{timestamp}_data.json`
- **내용**: 비디오 정보 + 자막 데이터
- **용도**: 원본 데이터 보관, 재처리

### 2. 프롬프트 파일 (Markdown)
- **파일명**: `{video_title}_{timestamp}_prompt.md`
- **내용**: Claude용 요약 생성 프롬프트
- **용도**: Claude에게 복사/붙여넣기

### 3. 이메일 초안 (HTML)
- **파일명**: `{video_title}_{timestamp}_email_draft.html`
- **내용**: 이메일로 보낼 HTML 내용
- **용도**: Gmail 전송 또는 수동 발송

## 고급 사용법

### 특정 Apify Actor 지정

```bash
python scripts/run_youtube_workflow.py \
  "URL" "YOUTUBE_KEY" "APIFY_KEY" \
  "email@example.com" \
  --actor "streamers/youtube-scraper"
```

### 출력 디렉토리 변경

```bash
python scripts/run_workflow_from_env.py \
  "URL" \
  --output "D:\YouTube_Summaries"
```

### 이메일 수동 전송

워크플로우가 이메일 초안을 생성한 후:

```bash
python scripts/send_email.py \
  "sender@gmail.com" \
  "app_password" \
  "recipient1@example.com,recipient2@example.com" \
  "YouTube 요약: Video Title" \
  "output/email_draft.html" \
  "output/prompt.md"
```

## 트러블슈팅

### 자막을 가져올 수 없음

**원인**:
- 비디오에 자막이 없음
- Apify Actor 문제
- API 할당량 초과

**해결**:
- 다른 Apify Actor 시도
- 자막 없이 메타데이터만 요약
- Apify 할당량 확인

### 이메일 전송 실패

**원인**:
- Gmail App Password 미설정
- SMTP 인증 오류
- 네트워크 문제

**해결**:
- App Password 재생성
- 이메일 초안 파일 수동 전송
- Gmail 보안 설정 확인

### 워크플로우 타임아웃

**원인**:
- 긴 비디오 (>1시간)
- 네트워크 느림
- Apify Actor 응답 지연

**해결**:
- 타임아웃 늘리기: `--timeout 600`
- 짧은 비디오로 테스트
- 네트워크 상태 확인

## 최적화 팁

### 1. 배치 처리

여러 영상을 한번에 처리:

```bash
#!/bin/bash
for url in $(cat video_urls.txt); do
  python run_workflow_from_env.py "$url"
  sleep 10  # API 할당량 고려
done
```

### 2. 선택적 자막

자막이 필요없는 경우 youtube-info만 사용:

```bash
python youtube-info/scripts/get_youtube_info.py "URL" "API_KEY"
```

### 3. 프롬프트 커스터마이징

`youtube-summary/assets/summary_template.md`를 수정하여 요약 형식 변경

## 통합 예제

### 완전 자동화 시나리오

```bash
# 1. .env 파일 준비
cat > .env << EOF
YOUTUBE_API_KEY=AIzaSy...
APIFY_API_KEY=apify_api_...
EMAIL_RECIPIENTS=team@company.com
GMAIL_SENDER=bot@company.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
OUTPUT_DIR=./summaries
EOF

# 2. 워크플로우 실행
python scripts/run_workflow_from_env.py \
  "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 3. 출력 확인
ls -l summaries/

# 4. Claude에게 요약 생성 요청
cat summaries/*_prompt.md | pbcopy  # macOS
# 또는
cat summaries/*_prompt.md | clip    # Windows

# 5. 생성된 요약을 이메일에 추가하여 전송
```

## API 비용 관리

### YouTube Data API
- **무료 할당량**: 10,000 units/day
- **비용**: 1 video = 1 unit
- **관리**: API 콘솔에서 모니터링

### Apify API
- **무료 할당량**: 5,000 compute units/month
- **비용**: 1 video captions = 10-50 units
- **관리**: Apify 대시보드에서 확인

### Gmail SMTP
- **무료**: 일일 500통까지
- **제한**: 앱 비밀번호 필요
- **관리**: Google 계정 설정

## 보안 고려사항

### API 키 보호
- `.env` 파일을 `.gitignore`에 추가
- 환경 변수 사용 권장
- 키 정기적으로 교체

### 이메일 보안
- Gmail App Password 사용 (일반 비밀번호 절대 사용 금지)
- SMTP over TLS 필수
- 수신자 목록 검증

### 데이터 관리
- 민감한 영상은 로컬 저장
- 자막 데이터 암호화 고려
- 정기적인 파일 정리

## 확장 아이디어

### 1. 데이터베이스 연동
요약 결과를 SQLite나 MongoDB에 저장

### 2. 웹 인터페이스
Flask/FastAPI로 웹 UI 구축

### 3. Slack 통합
요약 결과를 Slack 채널에 자동 게시

### 4. 정기 실행
Cron job으로 구독 채널 자동 요약

### 5. AI 요약 통합
Claude API 직접 호출하여 자동 요약 생성

## 문의 및 지원

- **문제 보고**: GitHub Issues
- **기능 요청**: GitHub Discussions
- **문서**: README.md 참조
