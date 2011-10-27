import os

# create a database table only in unit test mode
if os.environ['DJANGO_SETTINGS_MODULE'] == 'bootup.testsettings':
    from django.db import models
    from django.contrib.auth.models import User
    
    class UserProfile(models.Model):
        user = models.ForeignKey(User, related_name="%(class)s", unique=True)
        is_active = models.BooleanField(default=False)

        def __unicode__(self):
            return self.user.username



