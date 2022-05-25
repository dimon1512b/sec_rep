"""
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
"""
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
# future flag set to True so that we make full use of 2.0 style usage:
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))  # simple example
    print(f'{result = }')  # <sqlalchemy.engine.cursor.CursorResult object at 0x7f5b6ff1bc10>
    print(result.all())  # specific result
