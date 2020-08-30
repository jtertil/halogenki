import os

from flask import Flask
from logging import FileHandler, WARNING

from .database import Database


def create_app():
    """Create instance of Flask application."""
    # checks for the required environment variables
    required_env_var = [
        'FLASK_ENV',
        'DB_HOST',
        'DB_USER',
        'DB_PASS',
        'DB_PORT',
        'DB_NAME',
    ]

    for var in required_env_var:
        if not os.getenv(var):
            raise RuntimeError(f'{var} is not set.')

    if not os.getenv('FLASK_ENV') in ('development', 'testing', 'production'):
        raise RuntimeError('FLASK_ENV is not set to proper value.')

    # initiate flask app
    running_env = os.getenv('FLASK_ENV')
    app = Flask(__name__)

    # store db configuration in app config
    app.config['DATABASE_CONFIG'] = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'port': os.getenv('DB_PORT'),
        'dbname': os.getenv('DB_NAME')
        }

    if running_env == 'production':
        if app.debug:
            raise RuntimeError('Debug must be set off in production.')

        # error logging for production env
        f_handler = FileHandler('error_log.txt')
        f_handler.setLevel(WARNING)
        app.logger.addHandler(f_handler)

    elif running_env == 'development':
        app.config['TEMPLATES_AUTO_RELOAD'] = True

        # initiate database
        db = Database(app.config['DATABASE_CONFIG'])

        @app.route('/appstatus')
        def app_status():
            db_details = db.select_one('SELECT Version();')[0]
            return f'Flask is up and running in development config. ' \
                   f'Connected db: {db_details}.'

    elif running_env == 'testing':
        app.config['TESTING'] = True

        # initiate database
        db = Database(app.config['DATABASE_CONFIG'])

        # drop, recreate and insert default data into test database instance
        with app.open_resource('../sql/stock_drop_all.sql') as f:
            drop_all = f.read()
        db.execute(drop_all)

        with app.open_resource('../sql/stock_create_all.sql') as f:
            create_all = f.read()
        db.execute(create_all)

        with app.open_resource('../sql/stock_insert_default_data.sql') as f:
            insert_default_data = f.read()
        db.execute(insert_default_data)

        @app.route('/appstatus')
        def app_status():
            db_details = db.select_one('SELECT Version();')[0]
            return f'Flask is up and running in test config. ' \
                   f'Connected db: {db_details}.'

    return app
