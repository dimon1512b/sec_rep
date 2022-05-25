from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM some_table WHERE id>0 and id<10 and x between 0 and 10")
    )
    for dict_row in result.mappings():  # making row as python dict
        print(f'id = {dict_row.get("id")}, x = {dict_row.get("x")}')
