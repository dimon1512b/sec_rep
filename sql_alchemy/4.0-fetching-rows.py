from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://developer:secret@localhost:13306/developer", echo=True, future=True)
#  without manually commit
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM some_table WHERE x=0")
    )
    #  result it is iterable object
    #  Цікаво що коли ти проходишся по цьому резалту в циклі то його об'єкти зникають тобто виявляються одноразовими
    print(f'{result = }')
    case = 4  # варіанти отримання об'єктів бази
    if case == 1:
        for row in result:
            print(f'{row.id = }')
    elif case == 2:
        for col1, col2, col3 in result:
            print(f'{col1 = }, {col2 = }, {col3 = }')
    elif case == 3:
        for row in result:
            print(f'{row[0] = }')
    elif case == 4:
        for dict_row in result.mappings():  # making row as python dict
            print(f'{dict_row.get("id") = }')
    print(f'{result.all() = }')
    print('finished')
