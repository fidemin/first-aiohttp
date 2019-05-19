import argparse

from aiohttp import web

from routes import setup_routes
from settings import read_config

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='config file path')
args = parser.parse_args()
config = None

if args.config:
    config = read_config(args.config)

app = web.Application()
setup_routes(app)
if config:
    app['config'] = config
web.run_app(app)
