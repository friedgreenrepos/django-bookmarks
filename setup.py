import os
from setuptools import find_packages, setup
from bookmarks import __version__ as version_string

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bookmarks',
    version=version_string,
    description=(
        'Bookmarks for django web applications'
    ),
    long_description=README,
    author='gccallie',
    author_email='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'
    ],
    packages=find_packages(),
    include_package_data=True,
    license='',
    zip_safe=False,
    install_requires=[
        'Django>=2.1',
    ]
)
