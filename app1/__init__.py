import os

from psycopg2 import connect
from flask import Flask
from logging import FileHandler, WARNING


def create_app():
    """
    Create instance of Flask application.
    """

    if not os.getenv('FLASK_ENV') in ('development', 'testing', 'production'):
        raise RuntimeError('FLASK_ENV is not set to proper value.')

    app = Flask(__name__)
    run_env = os.getenv('FLASK_ENV')

    if run_env == 'production':
        if app.debug:
            raise RuntimeError('Debug must be off in production env.')

        # Error logging for production env.
        f_handler = FileHandler('error_log.txt')
        f_handler.setLevel(WARNING)
        app.logger.addHandler(f_handler)

    elif run_env == 'development':
        app.config['TEMPLATES_AUTO_RELOAD'] = True

        @app.route(f'/{app.name}')
        def index():
            return 'Flask is up and running in development config.'

    elif run_env == 'testing':
        app.config['TESTING'] = True

        # connect to dockerized postgres (only for testing)
        c = connect(
            dbname = 'postgres',
            user = 'postgres',
            host = '0.0.0.0',
            port = '5431',
            password = '1234'
        )


        @app.route(f'/{app.name}')
        def index():
            return 'Flask is up and running in test config.'

    return app

