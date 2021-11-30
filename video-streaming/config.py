import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PORT = os.environ.get('PORT')
    VIDEO_STORAGE_HOST = os.environ.get('VIDEO_STORAGE_HOST')
    VIDEO_STORAGE_PORT = int(os.environ.get('VIDEO_STORAGE_PORT'))
