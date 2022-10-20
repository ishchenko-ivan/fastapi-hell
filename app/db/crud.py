from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from db.config import DATABASE_URI
from db.models import Base

engine = create_engine(DATABASE_URI)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# s = Session()
# s.close()