import yaml

def read_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config
