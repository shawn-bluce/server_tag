
import json
import iterm2

from utils import color_text
from settings import config_file_name


class ServerConfig:
    def __init__(self, name: str, host: str, r: int, g: int, b: int):
        self.name = name
        self.host = host
        self.color = iterm2.Color(r, g, b)

    def __str__(self):
        return 'id:{}, server_name:{}, host:{}, color:{}'.format(
            id(self), self.name, self.host, self.color
        )


def get_server_list():
    server_list = []
    try:
        content = open(config_file_name).read()
        config = json.loads(content)
    except FileNotFoundError:
        color_text.warning('[WARNING] use default config, have no config file, '
                           'you can run `python3 generate_config.py` to create it.')
        return []
    except json.JSONDecodeError:
        color_text.error('[ERROR] use default config, because {} is invalid json data'.format(config_file_name))
        return []

    for group_name in config:
        group = config.get(group_name)
        color = group.get('color')
        r = color.get('R')
        g = color.get('G')
        b = color.get('B')
        for server_name, host_list in group.get('server').items():
            for server_host in host_list:
                server = ServerConfig(
                    server_name,
                    server_host,
                    r, g, b
                )
                server_list.append(server)

    return server_list
