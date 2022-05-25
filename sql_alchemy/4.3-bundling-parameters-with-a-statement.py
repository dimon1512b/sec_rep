"""
Opportunity to use method with values instead of list with values in SELECT
"""
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
stmt = text("SELECT * FROM some_table WHERE x < :x and y > x ORDER BY x, y").bindparams(x=10)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
