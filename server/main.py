import argparse

from aiohttp import web
import yaml

from routes import setup_routes

def read_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='config file path')
args = parser.parse_args()
config = read_config(args.config)

app = web.Application()
setup_routes(app)
app['config'] = config
web.run_app(app)
