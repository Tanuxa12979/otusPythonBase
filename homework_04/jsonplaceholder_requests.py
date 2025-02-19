"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from typing import List

import aiohttp
from fastapi import APIRouter

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data() -> List[dict]:
    response = await fetch(USERS_DATA_URL)
    return response


async def fetch_posts_data() -> List[dict]:
    response = await fetch(POSTS_DATA_URL)
    return response
