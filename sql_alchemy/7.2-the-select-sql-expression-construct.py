from sqlalchemy import select
from sqlalchemy import Table, create_engine, MetaData, insert

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)

metadata_obj = MetaData()

user_table = Table("user_account", metadata_obj, autoload_with=engine)
query = select(user_table).where(user_table.c.name == 'spongebob')

with engine.connect() as conn:
    sql_result = conn.execute(query)
    my_list = sql_result.mappings().all()
    print(f'{my_list = }')
    #  my_list = [{'id': 1, 'name': 'spongebob', 'fullname': 'Spongebob Squarepants'}]
