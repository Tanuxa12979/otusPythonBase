"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import nest_asyncio
from sqlalchemy import text

from models import async_session_factory, engine, Base, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


nest_asyncio.apply()

async def create_tables():
    async with engine.begin() as conn:
        # Создаем все таблицы
        await conn.run_sync(Base.metadata.create_all)


async def add_user(id: int, name: str, surname: str, email: str):
    async with async_session_factory() as session:
        async with session.begin():
            new_user = User(id=id, name=name, surname=surname, email=email)
            session.add(new_user)
        await session.commit()

async def add_post(id: int, title: str, body: str, user_id: int):
    async with async_session_factory() as session:
        async with session.begin():
            new_post = Post(id=id, title=title, body=body, user_id=user_id)
            session.add(new_post)
        await session.commit()


async def add_users(users_data):
    for user in users_data:
        await add_user(user["id"], user["name"], user["username"], user["email"])


async def add_posts(posts_data):
    for post in posts_data:
        await add_post(post["id"], post["title"], post["body"], post["userId"])


async def close_database():
    await engine.dispose()


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    await add_users(users_data)
    await add_posts(posts_data)
    await close_database()


def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()




#
# async def async_main():
#     async with async_session_factory() as session:
#         async with session.begin():
#             result = await session.execute(text("SELECT 'hello world'"))
#             print(result.all())


# Запуск асинхронной функции
# if __name__ == "__main__":
#     asyncio.run(create_tables())
    #asyncio.get_event_loop().run_until_complete(create_tables())
