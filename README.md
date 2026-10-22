# Hana Reservation — 은행 영업점 방문 예약 서비스

2022년 KAIST 전산학 교육과정 팀 프로젝트로 만든 Django 기반 영업점 방문 예약 웹 서비스입니다. 구현 전반을 담당했고, 2022년 6월 프로젝트 시연회에서 시연했습니다. 학습 목적의 프로젝트이며 실제 은행 서비스와는 관련이 없습니다.

## 주요 기능

- 영업점 목록·검색·페이지네이션, 지점 상세(네이버 지도 연동)
- 방문 예약 생성·조회·취소, 예약 문의 댓글
- 본인 예약만 수정·취소할 수 있도록 객체 단위 권한 검사
- 카카오·네이버 소셜 로그인(django-allauth), 이메일 인증
- 예약 완료·문의 답변 시 Twilio SMS 알림
- 지점 리뷰 댓글·좋아요, 사용자 팔로우, 직원·지점 모델

## 기술 스택

Python 3.8 · Django 2.2 (MVT) · django-allauth · Twilio · SQLite · HTML/CSS/JavaScript

## 실행 방법

```bash
python3.8 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # 필요한 값만 채우세요. 비워두면 소셜 로그인·SMS는 비활성
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 2026 보안 셀프 리뷰

공개에 앞서 2022년 코드를 다시 점검했고, 다음을 수정했습니다.

| 발견 사항 | 조치 |
|---|---|
| Django SECRET_KEY, OAuth Client Secret, Twilio 자격증명, SMTP 비밀번호가 소스에 하드코딩 | 모든 키 폐기·재발급 후 환경변수(`.env`)로 분리 |
| 실사용자 정보가 담긴 `db.sqlite3`, 업로드 이미지가 저장소에 포함 | 저장소에서 제외하고 `.gitignore` 적용 |
| 시크릿이 남아 있는 커밋 이력 | 새 저장소로 이력 없이 공개 |

남은 한계: 테스트 코드 부재, 운영 배포 설정(`DEBUG`, 정적 파일 서빙 등) 미정비. 학습 당시 코드를 최대한 그대로 보존했습니다.
