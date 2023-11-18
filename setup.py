
from setuptools import setup, find_packages
from sirocco.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sirocco',
    version=VERSION,
    description='sirocco, conversations with huggingface models',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='mojpg',
    author_email='john.doe@example.com',
    url='https://github.com/mojpg/sirocco/',
    license='MPL 2.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'sirocco': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        sirocco = sirocco.main:main
    """,
)
