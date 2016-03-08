# encoding: utf-8
"""
Configuration file. Please prefix application specific config values with
the application name.
"""

# Tokens
HARBOUR_CLIENT_ADSWS_API_TOKEN = 'TOKEN'

# Service URLs
VAULT_QUERY_URL = 'https://devapi.adsabs.harvard.edu/v1/vault/query'

# Log settings
TUGBOAT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/tmp/tugboat.log',
        },
        'console': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
