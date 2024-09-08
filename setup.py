from setuptools import setup, find_packages

setup(
    name='fbi_wanted_list',
    version='1.0.0',
    author='Arun Kumar Reddy Rayini',
    author_email='rayini.a@ufl.edu',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    description='A package for fetching and formatting FBI wanted data',
)
