"""
    Working with exist table without describe model
"""

from sqlalchemy import Table, create_engine, MetaData, insert

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)

metadata_obj = MetaData()

some_table = Table("some_table", metadata_obj, autoload_with=engine)

stmt = insert(some_table).values(x=123, y=321)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
