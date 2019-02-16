import os
from setuptools import (
    find_packages,
    setup,
)

VERSION = '0.3'
EXCLUDE_FROM_PACKAGES = ['tests']

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-wellknown',
    version=VERSION,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    long_description=README,
    dependency_links=open('dependency_links.txt').readlines(),
    install_requires=open('install_requires.txt').readlines(),
    scripts=['manage.py'],
)
