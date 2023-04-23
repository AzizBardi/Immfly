# Immfly Backend Test
### Description

I defined an API for a media platform that enables the display of content in a hierarchical structure. 
Each piece of content can consist of files such as videos, pdfs, or text, as well as arbitrary metadata, including content descriptions, authors, genre, and more. 
Additionally, each content item is assigned a rating value, which is a decimal number ranging from 0 to 10. 
Through this API, you can easily navigate through our media platform and access the information they need.


## How to run the project
### Docker
 - To run the project using docker
 > docker-compose -f deploy/docker-compose.yml up


### Localy

to run the project locally, you need :
- Python and Mysql 
- Create a database named 'immfly' or you can change the settings under the backendtest/setting
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "NAME": "immfly",
        "USER": "root",
        "PASSWORD": "admin",
        "OPTIONS": {},
    }
```
 - you can try to migrate (under the project root)
 ```sh
python manage.py migrate 
 ```
### Fixtures
 - To load some data use this command
> python manage.py loaddata media/fixtures/channels.json 

## Endpoint Description
 - access to swagger : 
> http://127.0.0.1:8000/api/schema/swagger-ui
 ```sh
api/media/channels/
```
 - List all the parent channels/groups
 - This list will show only channels without parents (Global channels)
 
 ```sh
api/media/channels/{slug}/
 ```
  - List a specific channel and all listed subchannels or listed content with the slug 
 
  ```sh
api/media/contents/{slug}/
 ```
  - List the content, and information about specific content with the slug

## Pytest

 - To run the pytest, you can run the command :
 ```sh
pytest
```


## CSV Generation
- To generate the rating CSV file use this command:
> python manage.py export_csv 

 - The file will be exported under the root project