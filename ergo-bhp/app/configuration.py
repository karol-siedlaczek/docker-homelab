import os
from django.core.management.utils import get_random_secret_key

SITE_NAME = 'Ergo BHP'  # Display name
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = '/data/media'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', default=get_random_secret_key())
ALLOWED_HOSTS = ['127.0.0.1', '*']
CSRF_TRUSTED_ORIGINS = ["https://ergobhp.com"]
DEBUG = False
TIME_ZONE = 'Europe/Zagreb'
LANGUAGE_CODE = 'pl-PL'  # Default lang if browser will not detect
DEFAULT_ORDERING = '-popularity'  # In category and subcategory views

LOG = {
    'MAX_SIZE': 1024 * 1024 * 5,  # 5MB
    'MAX_COUNT': 5,  # Per logger
    'LEVEL': os.getenv('LOG_LEVEL', default='DEBUG')  # DEBUG, INFO, WARNING, ERROR, CRITICAL
}

CACHE = {
    'ENABLED': True,
    'TTL': 3600
}

DATABASE = {  # PostgreSQL
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASS'),
    'HOST': os.getenv('DB_HOST', default='127.0.0.1'),
    'PORT': os.getenv('DB_PORT', default=5432),
    'CONN_MAX_AGE': os.getenv('DB_CONN_MAX_AGE', default=300)
}

SMTP_SERVER = {
    'USER': os.getenv('SMTP_USER'),
    'PASSWORD': os.getenv('SMTP_PASS'),
    'HOST': os.getenv('SMTP_HOST'),
    'PORT': os.getenv('SMTP_PORT', default=465),
}

REDIS = {
    'USER': os.getenv('REDIS_USER'),
    'PASSWORD': os.getenv('REDIS_PASS'),
    'HOST': os.getenv('REDIS_HOST', default='127.0.0.1'),
    'PORT': os.getenv('REDIS_PORT', default=6379),
    'SSL': os.getenv('REDIS_SSL', default=False)
}

CONTACT_FORM = {
    'MAX_PRODUCTS_PER_SUBMIT': 40,
    'MAX_ATTACHMENT_SIZE': 1024 * 1024 * 20,
    'MAX_ATTACHMENTS_PER_SUBMIT': 5,
    'RECIPIENT': 'ergobhp.info@gmail.com'
}

ALLOWED_FILE_EXTENSIONS = [
    'pdf', 'txt', 'doc', 'docx', 'odt', 'rtf', 'pptx',  # Documents
    'csv', 'xlsx', 'ods',  # Sheets
    'jpg', 'jpeg', 'png', 'svg', 'webp', 'ico', 'bmp', 'tiff', 'jfif'  # Images
    'zip', 'rar', '7zip', 'tar', 'gz',  # Packages
]
