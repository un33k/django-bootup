from django.conf import settings
from .fixtures import load_fixtures
from .users import setup_superuser
from .sites import setup_sites


# bootstrap the site with all info but only after the completion of syncdb
def bootup(sender, **kwargs):
    """
    After syncdb, bootstarp makes required adjustements in order to prepare and  to secure the site
    """
    # only trigger if we have installed the last app
    # print kwargs['app'].__name__ + " -- " + settings.INSTALLED_APPS[-1]+".models"
    if kwargs['app'].__name__ == settings.INSTALLED_APPS[-1]+".models":

        # 1. load the fixtures
        load_fixtures()

        # 2. setup sites
        setup_sites()

        # 3. setup an admin account
        setup_superuser(
            username=getattr(settings, 'ADMIN_NAME', ''),
            password=getattr(settings, 'MAIN_PASS', ''),
            email=getattr(settings, 'ADMIN_EMAIL', '')
         )




