#!/usr/bin/env python3
# generate template file config.json, when it not exists.
# run this command: `python3 generate_config.py`

import os
import json

from utils import color_text
from settings import config_file_name
from template_config import config as template_config

if __name__ == '__main__':
    file_content = json.dumps(template_config, indent=4)
    if os.path.exists(config_file_name):
        color_text.error('[error] {} is already exists, not generate.'.format(config_file_name))
        exit(1)
    else:
        open(config_file_name, 'w').write(file_content)
        color_text.success('[success] {} is generated.'.format(config_file_name))
