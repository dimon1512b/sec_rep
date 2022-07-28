import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

async_session = sessionmaker(
    create_async_engine(
        'mysql+aiomysql://developer:secret@127.0.0.1:13306/developer',
        future=True,
        pool_pre_ping=True,
        pool_use_lifo=True,
    ),
    expire_on_commit=False,
    class_=AsyncSession
)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def main() -> None:
    async with async_session() as session:
        query = 'SELECT * FROM domain'
        entities = await session.execute(query)
        print(f'{dir(entities.scalars()) = }')
        entities = entities.first()
        for entity in entities:
            print(f'{entity.domain_name = }')


if __name__ == '__main__':
    loop.run_until_complete(main())
