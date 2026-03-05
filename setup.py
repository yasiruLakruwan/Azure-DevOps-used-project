import os
from setuptools import setup,find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="AzureDevOps",
    author="Yasiru",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements
)


