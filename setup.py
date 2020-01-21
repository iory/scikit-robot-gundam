#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup_requires = []
install_requires = []

setup(
    name='scikit_robot_gundam',
    version='0.0.1',
    description='A python library',
    author='iory',
    author_email='ab.ioryz@gmail.com',
    url='https://github.com/iory/scikit-robot-gundam',
    license='MIT License',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
)
