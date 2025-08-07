from logging import config

config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
    },
})
