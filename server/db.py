import aiomysql
from aiomysql.sa import create_engine

from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

question = Table(
    'question', meta,

    Column('id', Integer, primary_key=True),
    Column('question_text', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)

choice = Table(
    'choice', meta,

    Column('id', Integer, primary_key=True),
    Column('choice_text', String(200), nullable=False),
    Column('votes', Integer, server_default="0", nullable=False),

    Column('question_id',
           Integer,
           ForeignKey('question.id', ondelete='CASCADE'))
)

async def init_mysql(app):
    conf = app['config']['mysql']
    engine = await create_engine(
        db=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        echo=True,
    )
    app['db'] = engine


async def close_mysql(app):
    db = app['db']
    db.close()
    await app['db'].wait_closed()
