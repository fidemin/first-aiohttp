
from aiohttp import web

from db import question

async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(question.select())
        ret = []
        async for row in cursor:
            ret.append(row.question_text)
    return web.json_response(ret)
