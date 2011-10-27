from django.conf import settings
from django.contrib.auth.models import User


def setup_superuser(username, password, email):
    """
    Create or update and account of type supersuer (fist user of this site)
    """
    if username and password and email:
        user, created = User.objects.get_or_create(pk=1)
        if user:
            user.username = username
            user.set_password(password)
            user.email = email
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
            user.save()