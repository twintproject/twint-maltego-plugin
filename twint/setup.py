#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='twint',
    author='Francesco Poldi (@noneprivacy)',
    version='1.0',
    author_email='francescopoldi@pielco11.ovh',
    description='Maltego extension for Twint',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    package_data={
        '': ['*.gif', '*.png', '*.conf', '*.mtz', '*.machine']  # list of resources
    },
    install_requires=[
        'canari>=3.3.9,<4'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
