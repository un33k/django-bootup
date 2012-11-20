# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from django.template import Context, Template
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from models import UserProfile

class BootupSuperuserTestCase(TestCase):
    """Tests for Django Bootup - Default Superuser """
    
    def test_manager(self):

        # username from testsettings
        username=getattr(settings, 'BOOTUP_SUPERUSER_NAME')
        email=getattr(settings, 'BOOTUP_SUPERUSER_EMAIL')
        superuser = User.objects.get(email=email)
        self.assertEquals(superuser.username, username)
        self.assertEquals(superuser.is_active, True)
        self.assertEquals(superuser.is_superuser, True)
        self.assertEquals(superuser.is_staff, True)
        
        # clean up
        User.objects.all().delete()

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
        
        # get the current site and it has to match the SITE_ID from the settings
        site = Site.objects.get_current()
        self.assertEquals(site.id, getattr(settings, 'SITE_ID'))

        # clean up
        Site.objects.all().delete()


if getattr(settings, 'BOOTUP_USER_PROFILE_AUTO_CREATE', False):
    class BootupUserProfileCreateTestCase(TestCase):
        """Tests for Django Bootup - User Profile Create"""
    
        def test_manager(self):
            # create a userprofile when a user is created
            username = "john"
            user, created = User.objects.get_or_create(username=username)
            self.assertEquals(user.username, username)
        
            # related profile has to exist
            profile = UserProfile.objects.get(user=user)
            self.assertEquals(profile.user, user)
        
            # clean up
            User.objects.all().delete()
        
            # clean up as the auto delete flag may not be set
            UserProfile.objects.all().delete()


if getattr(settings, 'BOOTUP_USER_PROFILE_AUTO_DELETE', False) and \
    getattr(settings, 'BOOTUP_USER_PROFILE_AUTO_CREATE', False):
    class BootupUserProfileDeleteTestCase(TestCase):
        """Tests for Django Bootup - User Profile Delete"""
    
        def test_manager(self):
            # create a userprofile when a user is created
            username = "john"
            user, created = User.objects.get_or_create(username=username)
        
            # related profile has to exist
            profile = UserProfile.objects.get(user=user)
            self.assertEquals(profile.user, user)
        
            username1 = "john1"
            user1, created = User.objects.get_or_create(username=username1)
        
            # related profile has to exist
            profile1 = UserProfile.objects.get(user=user1)
            self.assertEquals(profile1.user, user1)
        
            # delete the user1
            User.objects.all().delete()
        
            # related profile must have been delete as well
            profiles = UserProfile.objects.all()
            self.assertEquals(len(profiles), 0)






