import os
from django.conf import settings
from django.contrib.sites.models import Site

# setup the sites available for this project
def setup_sites():
    """
    Setup sites (name, domain) available for this project (SITE_ID will decide the active site)
    """
    site_info = getattr(settings, 'BOOTUP_SITES', None)
    if site_info:
        ids = site_info.keys()
        ids.sort()
        for id in ids:
            site, created = Site.objects.get_or_create(pk=id)
            if site:
                site.name = site_info[id]['name']
                site.domain = site_info[id]['domain']
                site.save()