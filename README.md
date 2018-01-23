# CKAN Harvester for OAI-PMH (Universidad de Zaragoza)

Based on https://github.com/openresearchdata/ckanext-oaipmh

## Instructions

### Installation

Use `pip` to install this plugin. This example installs it in `/var/www`


pip install -e git+https://github.com/aragonopendata/ckanext-oaipmh-unizar.git#egg=ckanext-oaipmh-unizar 
cd /var/www/ckanext-oaipmh
pip install -r ckanext-oaipmh-unizar/requirements.txt


Make sure the ckanext-harvest extension is installed as well.

**Important: You need to have a sysadmin user called "harvest" on your CKAN instance!**

### Setup the Harvester

- add `oaipmh_harvester_unizar` to `ckan.plugins` in `development.ini` (or `production.ini`)

