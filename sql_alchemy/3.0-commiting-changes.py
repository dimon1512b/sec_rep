from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
with engine.connect() as conn:
    result = conn.execute(text("CREATE TABLE IF NOT EXISTS some_table (id int AUTO_INCREMENT primary key, x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}])
    conn.commit()
