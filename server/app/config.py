import os
from dotenv import load_dotenv

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get("FLASK_ENV")
    TESTING = False
    DEBUG = False

    # Create development config
    if FLASK_ENV == "development":
        DEBUG = True
        
    # Create the testing config
    if FLASK_ENV == "testing":
        DEBUG = False
        TESTING = True

    # create the production config
    if FLASK_ENV == "production":
        DEBUG = False
