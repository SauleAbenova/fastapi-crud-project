🚀 FastAPI CRUD 애플리케이션

인공지능모델운영 (G952-2A0) 기말과제

이 프로젝트는 FastAPI, SQLAlchemy, SQLite를 활용하여 구현된 CRUD 시스템입니다.

📌 주요 기능

➕ 데이터 생성

📄 데이터 조회

✏️ 데이터 수정

❌ 데이터 삭제

🗄 SQLite 자동 데이터베이스 생성

🧩 Swagger UI 자동 문서화

🧠 사용 기술
기술	설명
FastAPI	Python 웹 프레임워크
SQLAlchemy	ORM
SQLite	내장형 DB
Uvicorn	ASGI 서버
Swagger UI	API 문서
📂 프로젝트 구조
fastapi-crud-project/
│
├── main.py
├── exam.db
└── README.md

⚙️ 실행 방법
1️⃣ 필요한 라이브러리 설치
pip install fastapi uvicorn sqlalchemy

2️⃣ 서버 실행
uvicorn main:app --reload

3️⃣ 브라우저에서 확인

Swagger UI 자동 문서화 페이지:

👉 http://127.0.0.1:8000/docs

🧪 API 사용 예시
➕ 데이터 생성 (POST /create)
{
  "title": "FastAPI 테스트",
  "content": "첫 번째 CRUD 아이템입니다!"
}

📄 전체 데이터 조회 (GET /items)
[
  {
    "id": 1,
    "title": "FastAPI 테스트",
    "content": "첫 번째 CRUD 아이템입니다!"
  }
]

✏️ 데이터 수정 (PUT /update/1)
{
  "title": "수정된 제목",
  "content": "수정된 내용입니다."
}

❌ 데이터 삭제 (DELETE /delete/1)
👩‍🎓 제작자

사울레 아베노바 (Saule Abenova)
경복대학교
인공지능모델운영 (G952-2A0)
2025년
