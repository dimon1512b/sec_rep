"""
Pydantic - it is library for work with JSON data

Expecting property name enclosed in double quotes!!! Ожидается что имя свойства будет заключено в двойные скобки

city_id: str = Field(alias='CityId') - This construction is for converting the variable name in JSON format into
a format convenient(удобный) for us.

print(city) - Returns the attributes of the city instance of a class City
print(city.json()) - Returns JSON with convenient variable for us
print(city.json(by_alias=True)) - Returns clean JSON

"""

from pydantic import BaseModel, Field


class City(BaseModel):
	citi_id: int = Field(alias='CityId')
	name: str
	population: int


input_Json = '{"CityId": "123", "name": "Moscow", "population": "1000000"}'

city = City.parse_raw(input_Json)

print(city)  # citi_id=123 name='Moscow' population=1000000
print(city.json())  # {"citi_id": 123, "name": "Moscow", "population": 1000000}
print(city.json(by_alias=True))  # {"CityId": 123, "name": "Moscow", "population": 1000000}
