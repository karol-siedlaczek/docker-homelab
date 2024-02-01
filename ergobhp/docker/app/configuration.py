BASE_URL = 'http://127.0.0.1:8080'
SITE_NAME = 'Ergo BHP'
SECRET_KEY = 'django-insecure-l_6n(71ug$n=a7sf^3^y6++ocm8rmuh_vn_!x75c0g7^)b=9eb'
ALLOWED_HOSTS = ['192.168.0.100', '127.0.0.1']
DEFAULT_ORDERING = '-popularity'
LOG_FILE_SIZE = 1024 * 1024 * 5  # 5MB
MAX_LOG_FILES = 5  # Per logger

DATABASE = {
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': 5432,
    'CONN_MAX_AGE': 300,
}

SMTP_SERVER = {
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': 465,
}

REDIS = {
    'USER': '',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': 6379,
    'SSL': False
}

CONTACT_FORM = {
    'MAX_PRODUCTS_PER_SUBMIT': 40,
    'MAX_ATTACHMENT_SIZE': 1024 * 1024 * 20,
    'MAX_ATTACHMENTS_PER_SUBMIT': 5,
    'RECIPIENT': 'karol@siedlaczek.org.pl'
}

ALLOWED_FILE_EXTENSIONS = [
    'pdf', 'txt', 'doc', 'docx', 'odt', 'rtf', 'pptx',  # documents
    'csv', 'xlsx', 'ods',  # sheets
    'jpg', 'jpeg', 'png', 'svg', 'webp', 'ico', 'bmp', 'tiff', 'jfif'  # img
    'zip', 'rar', '7zip', 'tar', 'gz',  # zip
]
