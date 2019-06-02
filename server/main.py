import argparse
import logging
import sys

from aiohttp import web

from routes import setup_routes
from settings import read_config
from db import init_mysql, close_mysql


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='config file path')
    args = parser.parse_args()

    if not args.config:
        print('[fatal] config flag is required')
        parser.print_help()
        sys.exit(2)

    config = read_config(args.config)

    app = web.Application()
    setup_routes(app)
    app['config'] = config
    app.on_startup.append(init_mysql)
    app.on_cleanup.append(close_mysql)
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)
