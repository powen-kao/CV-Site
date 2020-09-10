# CV Site
This site is built to update latest status of myself. Feel free to fork project for your own use. The theme is derived from free template on https://www.styleshout.com/.

Django framework is integrated to generate dynamic content in education, work and portfolio section. Those content can be modified through Django admin site directly. 

An apache server is hosted to serve static resources which is automatically collected on container creation.

Production site [kao.po-wen.de](https://kao.po-wen.de/)

Source on [Github](https://github.com/hp5588/CV-Site)

## Build
### Prepare
1. Install `docker`, `docker-compose` and `git`
1. Run `git pull https://github.com/hp5588/CV-Site`
1. Create proxy container and use let's encrypt for SSL connection \
    Refer to https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion
1. Modify `docker-compose.yml`,  `docker-compose-debug.yml` and `docker-compose-stage.yml` according to your need.\
    e.g. `proxy_tier` network interface is created for Nginx proxy; change to your own **domain**
    > `docker-compose.yml` is used on production server where `docker-compose-stage.yml` is meant to test image in pre-release domain before final deployment

### Production Build
1. Build docker image `docker build . -t hp5588/cv-kao:latest` \
   Skip this step if pull from docker hub
1. Run image with docker-compose `sudo docker-compose -f docker-compose.yml up -d --force-recreate`
  
### Debug Build
1. Build debug image `sudo docker build . -t dev-cv-kao:latest`
1. Run debug image with docker-compose `sudo docker-compose -f docker-compose-debug.yml up -d --force-recreate`\
    Debug mode is enabled and `cv-site` folder inside container is mapped to to root folder of repository

### CI
Docker image is automatically built on git push on master branch
https://hub.docker.com/r/hp5588/cv-kao

### Environment Variables
- ENV_DEBUG: whether Django debug is enabled. Should be disabled in production site for security reason (True/False)
- ENV_STATIC_URL: where you host static file such as html and CSS
- ENV_DB_KEY: password of your SQLite DB 
- ENV_LOCAL: whether use repository folder as MEDIA_ROOT (True/False)

## Customize
1. Visit `https://<your_domain.com>/admin` \
You might need to setup new password on first login
![Admin Site](https://github.com/hp5588/CV-Site/raw/master/images/admin_site.jpg)
2. Modify model data
3. Changes should be reflected at `https://<your_domain.com>` 

## Warning
- Security warning: DB password in `docker-compose.yml` should be replaced with your own password. Here shows only an example where to config password.