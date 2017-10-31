#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pandas-jalali.
# https://github.com/akolpakov/pandas-jalali

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Andrey Kolpakov <aakolpakov@gmail.com>

from setuptools import setup, find_packages

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox<2.0',
    'coveralls',
    'django_nose',
    'pypandoc',
    'khayyam'
]

setup(
    name='pandas-jalali',
    version='0.1.2',
    description='Manipulate with Jalali date in pandas',
    long_description=read_md('README.md'),
    keywords='python pandas jalali calendar',
    author='Andrey Kolpakov',
    author_email='aakolpakov@gmail.com',
    url='https://github.com/akolpakov/pandas-jalali',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        'numpy',
        'pandas'
    ],
    extras_require={
        'tests': tests_require,
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'django-unused-media=django-unused-media.cli:main',
        ],
    },
)
