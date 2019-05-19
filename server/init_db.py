import argparse

from sqlalchemy import create_engine, MetaData

from settings import read_config
from db import question, choice

DSN = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


def insert_sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'question_text': 'What\'s new?',
         'pub_date': '2015-12-15 17:17:49'}
    ])
    conn.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])
    conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='config file path')
    args = parser.parse_args()

    if not args.config:
        print("--config flag should be given")

    config = read_config(args.config)

    db_url = DSN.format(**config['mysql'])
    engine = create_engine(db_url)
    create_tables(engine)
    insert_sample_data(engine)
