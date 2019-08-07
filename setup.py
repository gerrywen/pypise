# coding=utf-8
import io

from pypise import __version__
from setuptools import find_packages, setup

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypise',
    version=__version__,
    description='WebUI automation testing framework based on Selenium and unittest.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='gerrywen',
    author_email='blog@gerrywen.com',
    url='https://github.com/gerrywen/pypise.git',
    license='MIT',
    packages=find_packages(exclude=['test.*', 'test']),
    package_data={},
    keywords='pypise pypise selenium testcase unittest',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'pypise=pypise.Pypise:main'
        ]
    }
)
