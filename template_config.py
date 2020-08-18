"""
    the template for server_tag config, don't edit this file.
    yourself config file is 'server_config.json', if you have no this file,
    can run this command: 'python3 generate_config.py' to create it.
"""

config = {
    'product': {
        'color': {
            'R': 255,
            'G': 0,
            'B': 0
        },
        'server': {
            'web': [
                '192.168.1.1',
                '192.168.1.2'
            ],
            'db': [
                '192.168.1.3',
                '192.168.1.4'
            ]
        }
    },
    'testing': {
        'color': {
            'R': 0,
            'G': 255,
            'B': 0,
        },
        'server': {
            'web': [
                '192.168.1.5',
                '192.168.1.6'
            ]
        }
    }
}
