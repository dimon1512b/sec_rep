"""
bulk_insert
"""
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
with engine.connect() as conn:
    count = conn.execute(text(
        "SELECT COUNT(*) FROM some_table"
    ))
    print(f'before {count.all() = }')
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": x, "y": x+1} for x in range(1000)]
    )
    conn.commit()
    count = conn.execute(text(
        "SELECT COUNT(*) FROM some_table"
    ))
    print(f'after {count.all() = }')
