from django.db.models import get_model
def fetch_model(name):
    """
    Return the model class for ``name`` in the following format:
    (name = app.model) -- Example:  (name = profile.UserProfile)
    If not profile found , None is returned
    """
    if name:
         return get_model(*name.split('.'))
