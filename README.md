# 🚀 FastAPI CRUD 애플리케이션  
**인공지능모델운영 (G952-2A0) 기말과제**

이 프로젝트는 **FastAPI**, **SQLAlchemy**, **SQLite**를 활용하여 구현한 간단하지만 완전한 기능을 갖춘 **CRUD(Create, Read, Update, Delete)** 시스템입니다.  
본 과제는 **경복대학교 인공지능모델운영 수업**의 기말과제로 수행되었습니다.

---

## 📌 주요 기능

- ➕ **Create** — 새로운 데이터 생성  
- 📄 **Read** — 모든 데이터 조회  
- ✏️ **Update** — ID 기준 데이터 수정  
- ❌ **Delete** — 데이터 삭제  
- 🗄 SQLite 데이터베이스 자동 생성  
- 🧩 Swagger UI를 통한 자동 문서화 지원  

---

## 🧠 사용 기술

| 기술 | 설명 |
|------|------|
| **FastAPI** | 현대적이고 빠른 Python 웹 프레임워크 |
| **SQLAlchemy** | ORM(Object Relational Mapper) |
| **SQLite** | 가벼운 내장형 데이터베이스 |
| **Uvicorn** | FastAPI 실행을 위한 ASGI 서버 |
| **Swagger UI** | API 자동 문서화 도구 |

---
fastapi-crud-project/
│
├── main.py # FastAPI 메인 애플리케이션 파일
├── exam.db # SQLite 데이터베이스 (자동 생성)
└── README.md # 프로젝트 설명 문서

---

## ⚙️ 실행 방법

### 1️⃣ 필요한 라이브러리 설치

```bash
pip install fastapi uvicorn sqlalchemy
2️⃣ 서버 실행
uvicorn main:app --reload

3️⃣ 브라우저에서 확인

Swagger UI 자동 문서화 페이지:

👉 http://127.0.0.1:8000/docs

🧪 API 사용 예시
➕ 데이터 생성

POST /create

{
  "title": "FastAPI 테스트",
  "content": "첫 번째 CRUD 아이템입니다!"
}

📄 전체 데이터 조회

GET /items

응답 예시:

[
  {
    "id": 1,
    "title": "FastAPI 테스트",
    "content": "첫 번째 CRUD 아이템입니다!"
  }
]

✏️ 데이터 수정

PUT /update/1

{
  "title": "수정된 제목",
  "content": "수정된 내용입니다."
}
❌ 데이터 삭제

DELETE /delete/1
제작자

사울레 아베노바 (Saule Abenova)
경복대학교
인공지능모델운영 (G952-2A0)
2025년

## 📂 프로젝트 구조

