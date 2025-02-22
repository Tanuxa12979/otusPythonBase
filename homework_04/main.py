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

from models import async_session_factory, engine, Base, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


nest_asyncio.apply()

async def create_tables():
    async with engine.begin() as conn:
        # Создаем все таблицы
        await conn.run_sync(Base.metadata.create_all)


async def add_posts(posts_data):
    async with async_session_factory() as session:
        async with session.begin():
            new_posts = [Post(id=post["id"], title=post["title"], body=post["body"], user_id=post["userId"]) for post in posts_data]
            session.add_all(new_posts)
        await session.commit()


async def add_users(users_data):
    async with async_session_factory() as session:
        async with session.begin():
            new_users = [User(id=user["id"], name=user["name"], username=user["username"], email=user["email"]) for user in users_data]
            session.add_all(new_users)
        await session.commit()


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
