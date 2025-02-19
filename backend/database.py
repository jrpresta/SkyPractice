
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""Setup a connection to Postgres and provide session"""

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def main():
    db = get_db()
    return db

if __name__ == '__main__':
    print(main())