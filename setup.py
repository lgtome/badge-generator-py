import os
import io
from platform import python_revision
from setuptools import setup, find_packages

NAME = 'py-badge-generator-naayaa-oops'
DESCRIPTION = 'Badge Generator app'
URL = 'https://github.com/NaaYaa-oops/badge-generator-py'
EMAIL = 'seryikotenok232@gmail.com'
AUTHOR = 'NaaYaa-oops'
REQUIRES_PYTHON = '>=2.7.18'
VERSION = '0.1.0'
KEYWORDS = 'py,generator,badges,gh'
REQUIRED = []
EXTRAS = []

absolute_path = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(absolute_path, 'README.md', encoding='utf-8') as file:
        file.read()
except FileNotFoundError:
    print(FileNotFoundError)


setup(
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    keywords=KEYWORDS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "/src"},
    packages=find_packages(where="src"),
    python_revision=REQUIRES_PYTHON
)
