DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'bootup',
]

DEBUG = TEMPLATE_DEBUG = True
MAIN_DOMAIN_NAME = 'example.com'
TEST_DOMAIN_NAME = 'example.net'
LOCAL_IP = '192.168.211.130'
LOCAL_PORT = "8080"
BOOTUP_SUPERUSER_NAME = "admin"
BOOTUP_SUPERUSER_PASSWORD = "mypasseh?"
BOOTUP_SUPERUSER_EMAIL = '{0}@{1}'.format(BOOTUP_SUPERUSER_NAME, MAIN_DOMAIN_NAME)

SITE_ID = 1
BOOTUP_SITES = {
    '1': {
        'name': 'production',
        'domain': MAIN_DOMAIN_NAME
    },
    '2':{
        'name': 'integration', # (optional)
        'domain': TEST_DOMAIN_NAME
    },
    '3': {
        'name': 'localhost', # development on local system (optional)
        'domain': 'localhost:{0}'.format(LOCAL_PORT)
    },
    '4':{
        'name': 'internal', # development on local or remote system such as headless vm!  (optional)
        'domain': '{0}:{1}'.format(LOCAL_IP, LOCAL_PORT)
    }   
}

# Django profiles
AUTH_PROFILE_MODULE = 'bootup.UserProfile'
BOOTUP_USER_PROFILE_AUTO_CREATE = True
BOOTUP_USER_PROFILE_AUTO_DELETE = True



