from app.db.config import SessionLocal
from app.user.models import User
from sqlalchemy import select


# insert or create user
def create_user(username: str, email: str, password: str):
    with SessionLocal() as session:
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        return user


def get_all_users():
    ## session exec() row database return karta hai. tuple foem  .
    ## scalars() directly colum ka value return karta hai. direct python objects/values.
    with SessionLocal() as session:
        stmt = select(User)
        result = session.scalars(stmt)
        return result.all()


def get_user(user_id: int):
    with SessionLocal() as session:
        stmt = select(User).where(User.id == user_id)
        result = session.scalars(stmt)
        return result.one()
