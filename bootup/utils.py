from django.db.models import get_model
def fetch_model(name):
    """
    Return the model class for ``name`` in the following format:
    (name = app.model) -- Example:  (name = profile.UserProfile)
    Or  return None
    """
    if name:
         return get_model(*name.split('.'))
    return None

