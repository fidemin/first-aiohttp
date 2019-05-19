
from aiohttp import web

from db import question

async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(question.select())
        async for row in cursor:
            print(row)
    return web.Response(text='Hello aiohttp')
