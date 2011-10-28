import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='django-bootup',
    version='0.8',
    description = "A Django bootup application that helps with quick and secure bootup of your django project",
    long_description = read('README'),
    author='Val L33',
    author_email='val@neekware.com',
    url='https://github.com/un33k/django-bootup',
    packages=['bootup'],
    #install_requires = [''],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )

