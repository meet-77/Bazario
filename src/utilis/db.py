from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from src.utilis.settings import settings

Base = declarative_base()

engine = create_engine(url=settings.DB_CONNECTION)

local_session = sessionmaker(bind=engine)

def get_db():
    session = local_session()
    try : 
        yield session
    finally:
        session.close()
