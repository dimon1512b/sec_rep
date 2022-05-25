from sqlalchemy import select, create_engine, MetaData, Table
from sqlalchemy.orm import Session, declarative_base

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)

metadata_obj = MetaData()

Base = declarative_base()


class User(Base):
    __table__ = Table("user_account", metadata_obj, autoload_with=engine)


query = select(User).where(User.id > 0).order_by(User.name)
with Session(engine) as session:
    result = session.scalars(query).all()
    for obj in result:
        print(f'{obj = }')  # obj = (<__main__.User object at 0x7fbfcc75bc40>,)
        print(f'{obj.name = }')  # obj.name = 'patrick'
