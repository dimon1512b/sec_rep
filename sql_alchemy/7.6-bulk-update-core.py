from sqlalchemy import bindparam, create_engine, MetaData, Table, update

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)

metadata_obj = MetaData()

user_table = Table('user_account', metadata_obj, autoload_with=engine)
stmt = (
  update(user_table).
  where(user_table.c.name == bindparam('oldname')).
  values(name=bindparam('newname'))
)
with engine.begin() as conn:
  conn.execute(
      stmt,
      [
         {'oldname': 'jack', 'newname': 'ed'},
         {'oldname': 'wendy', 'newname': 'mary'},
         {'oldname': 'jim', 'newname': 'jake'},
      ]
  )
