import configparser

config = configparser.ConfigParser()
config.read(r'bot_config.ini')

print(
    list(config['bot']['test'])
)

""""
{'bot': {'token': 'skjvkajsjkdh', 'admin_id': '123'}}
"""