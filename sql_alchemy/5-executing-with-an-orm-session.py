from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
stmt1 = text("SELECT x, y FROM some_table WHERE y < :y ORDER BY x, y").bindparams(y=6)
stmt2 = text("INSERT INTO some_table (x, y) VALUES (:x, :y)")
with Session(engine) as session:
    result = session.execute(stmt1)
    for row in result:
       print(f"x: {row.x}  y: {row.y}")
    session.execute(stmt2, [{'x': x, 'y': x**2} for x in range(5)])
    session.commit()
