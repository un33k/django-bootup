# -*- coding: utf-8 -*-
"""Unit tests for django bootup"""
from django.conf import settings
from django.test import TestCase
from django.template import Context, Template
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class BootupSuperuserTestCase(TestCase):
    """Tests for Django Bootup - Default Superuser """
    
    def test_manager(self):
        # we should have one user
        users = User.objects.all()
        self.assertEquals(len(users), 1)
        
        # username from testsettings
        username=getattr(settings, 'ADMIN_NAME', ''),
        admin = User.objects.get(pk=1)
        self.assertEquals(admin.is_active, True)
        self.assertEquals(admin.is_superuser, True)
        self.assertEquals(admin.is_staff, True)

class BootupSiteTestCase(TestCase):
    """Tests for Django Bootup - Default Sites"""
    
    def test_manager(self):
        # we should have 4 sites
        sites = Site.objects.all()
        self.assertEquals(len(sites), 4)
        
        # get the production site object
        site = Site.objects.get(name="production")
        self.assertEquals(site.domain, "example.com")
        
        site = Site.objects.get(name="integration")
        self.assertEquals(site.domain, "example.net")
