# CKAN Harvester for OAI-PMH (Universidad de Zaragoza)

Based on https://github.com/openresearchdata/ckanext-oaipmh

## Instructions

### Installation

1.  Install ckanext-harvest ([https://github.com/ckan/ckanext-harvest#installation](https://github.com/ckan/ckanext-harvest#installation)) (Only if you want to use the RDF harvester)

2. . /<CKAN_HOME>/bin/activate

3. cd <CKAN_HOME>/src

4.  Install the extension on your virtualenv:

    (pyenv)pip install -e git+https://github.com/aragonopendata/ckanext-oaipmh-unizar.git#egg=ckanext-oaipmh-unizar 


5.  Install the extension requirements:

        (pyenv) $ pip install -r ckanext-oaipmh-unizar/requirements.txt

6.  Enable the required plugins in your ini file:

        ckan.plugins = oaipmh_harvester_unizar


