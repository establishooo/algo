import os
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 25))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'false').lower() in ['true', '1', 't']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') 
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    broker_url = REDIS_URL
    result_backend = REDIS_URL
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    FRED_API_KEY = os.getenv('FRED_API_KEY')
    
    # إعدادات التخزين المؤقت
    CACHE_TYPE = 'filesystem'
    CACHE_DIR = 'cache'
    CACHE_DEFAULT_TIMEOUT = 3600  # 1 ساعة
    
    # إعدادات التسجيل
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LOG_LEVEL = logging.DEBUG

    # Polygon API
    POLYGON_API = os.getenv('POLYGON_API')
    POLYGON_NAME = os.getenv('POLYGON_NAME')
    POLYGON_KEY_ID = os.getenv('POLYGON_KEY_ID')

    # Alpha Vantage API
    ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
