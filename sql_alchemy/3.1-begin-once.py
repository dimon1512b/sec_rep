from sqlalchemy import create_engine, text
engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
#  without manually commit
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    )
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 0, "y": 0}, {"x": 0, "y": 1}]
    )
    result = conn.execute(
        text("SELECT * FROM some_table WHERE x=0")
    )
    #  result it is iterable object
    #  Цікаво що коли ти проходишся по цьому резалту в циклі то його об'єкти зникають тобто виявляються одноразовими
    print(f'{result = }')
    for row in result:
        print(f'{row.id = }')
    print(f'{result.all() = }')
    print('finished')
