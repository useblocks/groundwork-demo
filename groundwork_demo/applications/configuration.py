import sys
import os

APP_NAME = "groundwork_demo_app"
APP_DESCRIPTION = "groundwork application of package groundwork-demo"
APP_PATH = os.path.dirname(__file__)

FLASK_SERVER_NAME = "127.0.0.1:5000"

GROUNDWORK_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "%(asctime)s - %(levelname)-5s - %(message)s"
        },
        'debug': {
            'format': "%(asctime)s - %(levelname)-5s - %(name)-40s - %(message)-80s - %(module)s:%("
                      "funcName)s(%(lineno)s)"
        },
    },
    'handlers': {
        'console_stdout': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'level': 'INFO'
        },
        'file': {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "debug",
            "filename": "logs/app.log",
            "maxBytes": 1024000,
            "backupCount": 3,
            'level': 'DEBUG'
        },
        # 'file_my_plugin': {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "formatter": "debug",
        #     "filename": "logs/my_plugin.log",
        #     "maxBytes": 1024000,
        #     "backupCount": 3,
        #     'level': 'DEBUG'
        # },
    },
    'loggers': {
        '': {
            'handlers': ['console_stdout'],
            'level': 'DEBUG',
            'propagate': False
        },
        'groundwork': {
            'handlers': ['console_stdout', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        # 'MyPlugin': {
        #     'handlers': ['console_stdout', 'file_my_plugin'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
    }
}


