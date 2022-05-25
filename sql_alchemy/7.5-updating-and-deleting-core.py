from sqlalchemy import update, create_engine, MetaData, Table

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)

metadata_obj = MetaData()

user_table = Table('user_account', metadata_obj, autoload_with=engine)

stmt = (
    update(user_table).where(user_table.c.name == 'patrick').
    values(fullname='Patrick the Star')
)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
