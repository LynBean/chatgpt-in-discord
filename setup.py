#!/usr/bin/env python3

from setuptools import setup, find_packages
import os
import re
import sys

with open('README.md', 'r', encoding = 'UTF-8') as README :
    LONG_DESCRIPTION = README.read()

PATH = os.path.join(os.path.dirname(__file__), 'src')
FILE_PATH = os.path.join(PATH, '__init__.py')

def get_version():
    with open(FILE_PATH, 'r', encoding = 'UTF-8') as f:
        for line in f:
            m = re.match("__version__ = '(.*)'", line)
            if m:
                return m.group(1)

    raise SystemExit('Could not find version string.')


if sys.version_info < (3, 8):
    sys.exit('Requires Python >= 3.8.')


setup(
    name = 'chatgpt-in-discord',
    version = get_version(),
    description = 'ChatGPT now in Discord!',
    author = 'Kim',
    author_email = '2003victoryy@gmail.com',
    url = 'https://github.com/LynBean/chatgpt-in-discord',
    packages = find_packages(exclude = ['tests']),
    zip_safe = False,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    python_requires = '>=3.8',
    install_requires = [
        'asyncio',
        'discord',
        'openai',
        ],
    entry_points = {
        'console_scripts': ['chatgpt-in-discord = src._main: main'],
    },
    classifiers = [
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
)