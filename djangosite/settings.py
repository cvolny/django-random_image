import os
import imp


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ('localhost', 'python33-thevolny.rhcloud.com', 'www.randomdick.pics')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'sorl.thumbnail',
    'random_image',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangosite.urls'
WSGI_APPLICATION = 'djangosite.wsgi.application'
if ON_OPENSHIFT:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     os.environ['OPENSHIFT_APP_NAME'],
            'USER':     os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
            'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
            'HOST':     os.environ['OPENSHIFT_MYSQL_DB_SOCKET'],
            'PORT':     '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

SITE_ID = 1
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
APPEND_SLASH = False
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', os.path.join(BASE_DIR, 'media'))


default_keys = {'SECRET_KEY': 'z^jvcflogam45zw)+h*@nhh%$h#gnr!*agx_rkm=yfdl10(jtm'}
use_keys = default_keys
if ON_OPENSHIFT:
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)
SECRET_KEY = use_keys['SECRET_KEY']
