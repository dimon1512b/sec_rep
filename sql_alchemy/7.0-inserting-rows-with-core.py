from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, insert

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

stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")

case = 2


if case == 1:
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

#  OR

elif case == 2:
    with engine.connect() as conn:
        result2 = conn.execute(
            insert(user_table),
            [
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "patrick", "fullname": "Patrick Star"}
            ]
        )
        conn.commit()
