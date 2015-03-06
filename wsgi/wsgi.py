#!/usr/bin/env python

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")
from django.conf import settings

if settings.ON_OPENSHIFT:
    sys.path.append(os.environ['OPENSHIFT_REPO_DIR'])
    virtenv = os.environ['VIRTUAL_ENV']
    os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
    virtualenv = os.path.join(virtenv, 'bin/activate')
    # noinspection PyBroadException
    try:
        os.system(virtualenv)
    except:
        pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()