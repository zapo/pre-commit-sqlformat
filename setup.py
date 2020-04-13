from setuptools import setup

setup(
    name='pre-commit-sqlformat',
    description='a pre-commit hook for formatting sql',
    version='0.0.1',
    install_requires=[
        'sqlparse'
    ],
)
