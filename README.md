# CV Site
This site is built to update latest status of myself and for job searching. Feel free to fork project for your own use. The theme is derived from template on https://www.styleshout.com/ and modified accordingly to my need.

Django framework is integrated to generate dynamic content in education and work section. Those content can be modified through Django admin site directly. 

An apache server is hosted to serve static resources which is automatically collected on container creation.

Production site [kao.po-wen.de](https://kao.po-wen.de/)

Source on [Github](https://github.com/hp5588/CV-Site)

## Build
### Prepare
1. Install ``docker`` and ``docker-compose``
1. Build docker image ``docker build .`` \
    Ignore this if pull from docker hub

### CI
Docker image is automatically built on git push on master branch
https://hub.docker.com/r/hp5588/cv-kao

## Deployment  
### Steps
1. Create proxy container and use let's encrypt for SSL connection \
 Refer to https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion
1. Modify ``docker-compose.yml`` file according to your need.\
    e.g. ``proxy_tier`` network interface is created for Nginx proxy; change to your own domain
1. Run with docker compose ``docker-compose up -d``. 

### Environment Variables
- ENV_DEBUG: should be disabled in production site for security reason
- ENV_STATIC_URL: where you host static file such as html and CSS
- ENV_DB_KEY: password of you SQLite DB 




## Warning
Security warning: DB password in ``docker-compose.yml`` should be replaced with your own password. Here we only show an example of where to config password.