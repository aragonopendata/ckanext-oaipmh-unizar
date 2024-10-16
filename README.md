# ckanext-oaipmh-unizar
Esta extensión añade funcionalidades a 'ckanext-harvest' para tener la opción de cosechar datos de un sistema con protocolo 'OAI - PMH', en este caso está adaptado para tartar los datos obtenidos de 'Universidad de Zaragoza'.
Para utilizar esta nueva funcionalidad de 'ckanext-haverst', tras añadir el plugin a CKAN, entra en el entorno WUI o CLI de 'ckanext-haverst' y crea un nuevo 'source' del tipo 'OAI-PMH' (en el entorno WUI lo veremos como 'OAI-PMH').

## Instalación
Para instalar ckanext-oaipmh-unizar:

1. Añade la siguiente línea a tu Dockerfile:
    ``` Dockerfile
     RUN pip install -e git+https://github.com/aragonopendata/ckanext-oaipmh-unizar.git@master#egg=ckanext-oaipmh-unizar  && \
         pip install -r ${APP_DIR}/src/ckanext-oaipmh-unizar/requirements.txt
    ```

2. Añade 'iaest_rdf_harvester' a los plugins de CKAN

3. Construye y levanta el entorno de CKAN.
    ```bash
    cd entorno_de_ckan
    docker compose build
    docker compose up -d
    ```
