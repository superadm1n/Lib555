#!/usr/bin/env python
from setuptools import setup

description = '''Package to easily preform calculations of monostable and astable 555 timer circuits'''

setup(
    name='Lib555',
    version='1.0',
    packages=['Lib555'],
    keywords='555 timer',
    url='https://github.com/superadm1n/Lib555',
    license='MIT',
    author='Kyle Kowalczyk',
    author_email='kowalkyl@gmail.com',
    description=description,
    long_description=description,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ]
)
