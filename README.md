## Create virtual environment command
python -m venv venv
## Activate venv environment command
venv/Scripts/activate
## Deactivate command
deactivate
## Fast Api install command
pip install  "fastapi[standard]"
- pydantic
 - email-validator
- starlette
 - httpx
 - jinja2
 - python-multipart
 - uvicorn
## Run fast api command
fastapi dev main.py
## Two Types Of Structure 
- Horizontal and Vertical Structure
 - Horizontal Structure (Layered by Responsibility)
This structure separates the project into layers based on functionality type — good for small to medium apps.
    app/
    ├── routers/
    │   ├── users.py
    │   └── items.py
    ├── models/
    │   ├── user.py
    │   └── item.py
    ├── schemas/
    │   ├── user_schema.py
    │   └── item_schema.py
    ├── services/
    │   ├── user_service.py
    │   └── item_service.py
    ├── main.py
 - Pros:
    - Clear separation of concerns
    - Easy to onboard new devs
 - Cons:
    - Cross-feature changes require touching multiple folders
    - Can get messy as features grow
- This structure groups everything by feature domain — ideal for large, scalable apps.
follow domain draggon design also called feature based strucutre.
    app/
    ├── users/
    │   ├── router.py
    │   ├── model.py
    │   ├── schema.py
    │   └── service.py
    ├── items/
    │   ├── router.py
    │   ├── model.py
    │   ├── schema.py
    │   └── service.py
    ├── core/
    │   ├── config.py
    │   └── security.py
    ├── main.py
 - Pros:
    - Feature encapsulation (easy to test, refactor, reuse)
    - Scales well with microservices or domain-driven design
 - Cons:
    - Slightly harder for beginners to navigate
    - Requires discipline in naming and boundaries
    
## --init_.py create package our folder in angular


## SQLAlchemy synchronous install command
pip install SQLAlchemy


## import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

 
## install alembic
pip install alembic

alembic init alembic

## async alembic
 alembic init  -t async alembic

## config file
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine, expire_on_commit=False, autocommit=False, autoflush=False
)

## create a migration script 
alembic revision --autogenerate -m "create users table"

## migration script
alembic upgrade head

## see requirements.txt
 pip freeze > requirements.txt 

## async sqlalchemy install command
pip install sqlalchemy[asyncio]

## import sqlalchemy 
 import sqlalchemy

## sqlit commands
 pip install aiosqlite



