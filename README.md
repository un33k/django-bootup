Django Bootup Application
====================

**A Django application that takes care of the repetitive tasks of starting and running a clean project.**

**Author:** Val Neekman, [ info@neekware.com, @vneekman]

Overview
========

Bootup can create your superuser automatically, setup your sites objects, create and delete your
UserProfiles when a User is created or delete and even load up your initial fixtures in a deterministic way.

How to install
==================

    1. easy_install django-bootup
    2. pip install django-bootup
    3. git clone http://github.com/un33k/django-bootup
        a. cd django-bootup
        b. run python setup.py
    4. wget https://github.com/un33k/django-bootup/zipball/master
        a. unzip the downloaded file
        b. cd into django-bootup-* directory
        c. run python setup.py

How to use
=================

    Stick ``"bootup"`` in ``INSTALLED_APPS``, right after all other Django specific Apps
    Follow the instruction in the ``Current Features`` at the top of this file for usage.
    Run syncdb and enjoy


Running the tests
=================

    To run the tests against the current environment:
    python manage.py test bootup


Current Features
=================

    1. Disable ``syncdb`` from prompting you to create a superuser

    2. Latch on the ``post_syncdb`` signal and execute the following:
        A. Install all ``fixture(s)`` found within a given path (single path)
            * - Path is set in your settings file as: BOOTUP_INITIAL_FIXTURES_DIRS
            * _ Any valid fixture file(s) at the above path will be installed
            * _ Fixture files(s) at the above path don't require to start with ``initial_``
            * _ Fixture installation will be skipped if no fixture file is found at the specified path
            * _ Fixture installation will be skipped if BOOTUP_INITIAL_FIXTURES_DIRS is not defined or empty
            * _ Warning: fixture(s) in this directory will be loaded after ``each`` syncdb and wipe your changes out

        B. Create or Update a superuser
            * - This superuser will be the first created user on your system
            * - Primary Key = ``1`` will be used to fetch and update existing superuser
            * - Superuser credentials have to be set in the project's settings file as follows:
              + BOOTUP_SUPERUSER_NAME = "desired name for the superuser"
              + BOOTUP_SUPERUSER_PASSWORD = "desired password for ``the`` superuser"
              + BOOTUP_SUPERUSER_EMAIL = "desired email address for the superuser"
            * _ Superuser creation/update will be skipped if:
              + Any of the three (above) credentials is undefined or empty

        C. Automatically create the required ``Site`` objects with proper ``name`` and ``domain`` if:
            * _ Existence of BOOTUP_SITES in your setting file with the following format
            # -------------------------------
            BOOTUP_SITES = {
                '1': {
                    'name': 'Example Inc',  # production site
                    'domain': 'example.com'
                },
                '2':{
                    'name': 'integration', # (optional)
                    'domain': 'example.net'
                },
                '3': {
                    'name': 'localhost', # development on local system (optional)
                    'domain': 'localhost:8080'
                },
                '4':{
                    'name': 'internal', # development on local or remote system such as headless vm!  (optional)
                    'domain': '10.10.1.50:8080'
                }   
            }
            # -------------------------------
            * _ SITE_ID needs to be set to an index to one of the above fields in BOOTUP_SITES
                + For the Production server set SITE_ID = "1"
                + For the Integration server set SITE_ID = "2"
                + For the Localhost server set SITE_ID = "3"
                + For a IP based server set SITE_ID = "4"
            * _ Any existing site objects with (pk= 1,2,3,4) will be updated with the relevant info set in BOOTUP_SITES
            * _ Site creation will be skipped if BOOTUP_SITES is not defined in your settings file

    4. Automatically create a matching user profile ``anytime`` after each user creation if:
        A. Existence of BOOTUP_USER_PROFILE_AUTO_CREATE = True in your settings file
        B. Existence of AUTH_PROFILE_MODULE = 'application.UserProfile' in your settings file
            * _ Example ``AUTH_PROFILE_MODULE = profile.UserProfile'``
        C. User profile creation will be skipped if:
            * _ BOOTUP_USER_PROFILE_AUTO_CREATE is set to False or empty or not set in your settings file
            * _ AUTH_PROFILE_MODULE is empty, invalid or not set in your setting file
            * _ AUTH_PROFILE_MODULE points to an application and module that is incomplete or misconfigured

    5. Automatically delete a matching user profile ``anytime`` after each user deletion if:
        A. Existence of BOOTUP_USER_PROFILE_AUTO_CREATE = True in your settings file
        B. Existence of BOOTUP_USER_PROFILE_AUTO_DELETE = True in your settings file
        C. Existence of AUTH_PROFILE_MODULE = 'application.UserProfile' in your settings file
            * _ Example ``AUTH_PROFILE_MODULE = profile.UserProfile'``
        D. User profile deletion will be skipped if:
            * _ BOOTUP_USER_PROFILE_AUTO_DELETE is set to False or empty or not set in your settings file
            * _ AUTH_PROFILE_MODULE is empty, invalid or not set in your setting file
            * _ AUTH_PROFILE_MODULE points to an application and module that is incomplete or misconfigured


Changelog
=========

1.0.1
-----
* move away from buildout
* add .travis.yml
* changed version format

0.1
-----
* initial release
* disable syncdb prompt to generate superuser
* auto generate superuser post syncdb
* auto generate site(s) object

License
=======

Copyright © Val Neekman

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



