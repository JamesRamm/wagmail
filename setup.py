#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111,W6005,W6100
from __future__ import absolute_import, print_function

import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('wagmail', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')).read()

setup(
    name='wagmail',
    version=VERSION,
    description="""Build, send & schedule emails from the Wagtail admin""",
    long_description=README + '\n\n' + CHANGELOG,
    author='James Ramm',
    author_email='ramshacklerecording@gmail.com',
    url='https://github.com/JamesRamm/wagmail',
    packages=[
        'wagmail',
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.8,<1.11",
        "Wagtail>=1.7"
    ],
    license="AGPL 3.0",
    zip_safe=False,
    keywords='Django Wagtail',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
