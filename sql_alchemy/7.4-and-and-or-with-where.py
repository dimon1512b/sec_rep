from sqlalchemy import and_, or_, select, create_engine, MetaData, Table
from sqlalchemy.orm import Session, declarative_base

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)

metadata_obj = MetaData()

Base = declarative_base()


class User(Base):
    __table__ = Table("user_account", metadata_obj, autoload_with=engine)


class Address(Base):
    __table__ = Table("address", metadata_obj, autoload_with=engine)


query = select(Address.email_address) \
    .where(and_(or_(User.name == 'squidward', User.name == 'sandy'), Address.user_id == User.id))

with Session(engine) as session:
    result = session.scalars(query).all()
    for obj in result:
        print(f'{obj = }')
