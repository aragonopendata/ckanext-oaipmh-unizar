from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-oaipmh-unizar',
    version=version,
    description="OAI-PMH Universidad de Zaragoza Harvester for CKAN ",
    long_description="",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Opendata',
    author_email='opendata@aragon.es',
    url='http://www.liip.ch',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.oaipmh-unizar'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    oaipmh_harvester_unizar=ckanext.oaipmh.harvester:OaipmhHarvester
    [paste.paster_command]
    harvester_unizar=ckanext.oaipmh.command:OaipmhHarvesterCommand
    """,
)
