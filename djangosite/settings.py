import os
import imp


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ON_OPENSHIFT = 'OPENSHIFT_REPO_DIR' in os.environ

DEBUG = not ON_OPENSHIFT
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ('localhost', 'python33-thevolny.rhcloud.com', 'randomdick.pics')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'compressor',
    'jquery',
    'jquery_ui',
    'jquery_lightbox',
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

WSGI_APPLICATION = 'djangosite.wsgi.application'
ROOT_URLCONF = 'djangosite.urls'
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
USE_LIGHTBOX = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR', BASE_DIR), 'static')
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
COMPRESS_ENABLED = not DEBUG
COMPRESS_OUTPUT_DIR = "cache"
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


default_keys = {'SECRET_KEY': 'z^jvcflogam45zw)+h*@nhh%$h#gnr!*agx_rkm=yfdl10(jtm'}
use_keys = default_keys
if ON_OPENSHIFT:
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)
SECRET_KEY = use_keys['SECRET_KEY']
