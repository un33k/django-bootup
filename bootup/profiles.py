from django.conf import settings
from .utils import fetch_model

def get_profile_model():
    """
    Return the model class for the user profile, as defined by the 
    ``AUTH_PROFILE_MODULE`` setting. Or None
    """
    profile_module = getattr(settings, 'AUTH_PROFILE_MODULE', '')
    if profile_module:
        profile_model = fetch_model(profile_module)
        if profile_model:
            return profile_model
    return None

def create_profile(sender, instance, created, **kwargs):
    """
    Create a matching profile whenever a user object is created.
    if settings.BOOTUP_USER_PROFILE_AUTO_CREATE is not defined or False, 
    the auto profile creation is skipped
    """
    profile_model = get_profile_model()
    if profile_model:
        if created:
            try:
                p, c = profile_model.objects.get_or_create(user=instance)
            except:
                pass

def delete_profile(sender, instance, **kwargs):
    """
    Delete a matching profile whenever a user object is deleted.
    if settings.BOOTUP_USER_PROFILE_AUTO_DELETE is not defined or False, 
    the auto profile creation is skipped
    """
    profile_model = get_profile_model()
    if profile_model:
        try:
            profile_model.objects.get(user=instance).delete()
        except:
            pass





