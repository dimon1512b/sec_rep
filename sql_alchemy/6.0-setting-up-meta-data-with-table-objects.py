from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, Integer, String


engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
metadata_obj = MetaData()
user_table = Table(
    "user_account",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String(30))
)

metadata_obj.create_all(bind=engine)
