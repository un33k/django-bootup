import os
try:
    _s = os.environ['DJANGO_SETTINGS_MODULE']
except KeyError:
    # settings should have been set by now, if not, we must be in test mode
    os.environ['DJANGO_SETTINGS_MODULE'] = 'bootup.testsettings'

from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app
from .bootup import bootup

# disable syncdb from prompting you to create a superuser.
# we need a superuser, so we let fixtures to create it for us.
signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_app,
    dispatch_uid = "django.contrib.auth.management.create_superuser")

# bootstrap our project (site) after syncdb
signals.post_syncdb.connect(bootup)

