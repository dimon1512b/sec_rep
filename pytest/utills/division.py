from pydantic import PositiveInt


def division(a, b: PositiveInt) -> float:
    if PositiveInt(b):
        return a / b
    else:
        return 'Division by zero!'
