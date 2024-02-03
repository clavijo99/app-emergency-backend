# app-example

- Django 4.0.4
- Postgres 12
- Dokku
- push notification 
## Push Notification Support

- Android: Push notifications are supported on Android devices using Firebase Cloud Messaging (FCM). You can integrate FCM into your Android app to enable push notifications.

- iOS: Push notifications are supported on iOS devices using Apple Push Notification service (APNs). You can configure your iOS app with APNs to enable push notifications.

- Web: Push notifications are supported on web browsers using the Web Push API. You can implement web push notifications in your web application to send notifications to users on supported browsers.
## config (Production Ready)

## Documentation ##

### Directory Tree ###
```

├── main (Main application of the project, use it to add main templates, statics and root routes)
│   ├── fixtures
│   │   ├── dev.json (Useful dev fixtures, by default it creates an `admin` user with password `admin`)
│   │   └── initial.json (Initial fixture loaded on each startup of the project)
│   ├── migrations
│   ├── static (Add here the main statics of the app)
│   ├── templates (Add here the main templates of the app)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py (Main models like City, Config)
│   ├── tests.py (We hope you will put some tests here :D)
│   ├── urls.py (Main urls, place the home page here)
│   └── views.py
├── media
├── app-example
│   ├── settings
│   │   ├── partials
│   │   │   └── util.py (Useful functions to be used in settings)
│   │   ├── common.py (Common settings for different environments)
│   │   ├── development.py (Settings for the development environment)
│   │   └── production.py (Settings for production)
│   ├── urls.py
│   └── wsgi.py
├── scripts
│   ├── command-dev.sh (Commands executed after the development containers are ready)
│   └── wait-for-it.sh (Dev script to wait for the database to be ready before starting the django app)
├── static
├── Dockerfile (Instructions to create the project image with docker)
├── Makefile (Useful commands)
├── Procfile (Dokku or Heroku file with startup command)
├── README.md (This file)
├── app.json (Dokku deployment configuration)
├── docker-compose.yml (Config to easily deploy the project in development with docker)
├── manage.py (Utility to run most django commands)
└── requirements.txt (Python dependencies to be installed)
```

### How to install the template ###

Clone the repository, and update your origin url: 
```
git clone https://github.com/clavijo99/django-postgres-dokku app-example
cd app-example
```
Rename your project files and directorys:
```
make name=app-example init
```
> Info: Make is required, for mac run `brew install make`

> After this command you can already delete the init command inside the `Makefile` 

The command before will remove the `.git` folder so you will have to initialize it again:
```
git init
git remote add origin <repository-url>
```

### How to run the project ###

The project use docker, so just run:

```
docker-compose up
```

> If it's first time, the images will be created. Sometimes the project doesn't run at first time because the init of postgres, just run again `docker-compose up` and it will work.

*Your app will run in url `localhost:8000`*

To recreate the docker images after dependencies changes run:

```
docker-compose up --build
```

To remove the docker containers including database (Useful sometimes when dealing with migrations):

```
docker-compose down
```

### Accessing Administration

The django admin site of the project can be accessed at `localhost:8000/admin`

By default the development configuration creates a superuser with the following credentials:

```
Username: admin
Password: admin
```

## Production Deployment: ##

The project is dokku ready, this are the steps to deploy it in your dokku server:

#### Server Side: ####

> This docs does not cover dokku setup, you should already have configured the initial dokku config including ssh keys

Create app and configure postgres:
```
dokku apps:create app-example
dokku postgres:create app-example
dokku postgres:link app-example app-example
```

> If you don't have dokku postgres installed, run this before:
> `sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git`

Create the required environment variables:
```
dokku config:set app-example ENVIRONMENT=production DJANGO_SECRET_KEY=....
```

Current required environment variables are:

* ENVIRONMENT
* DJANGO_SECRET_KEY
* EMAIL_PASSWORD

Use the same command to configure secret credentials for the app

#### Local Side: ####

Configure the dokku remote:

```
git remote add production dokku@<my-dokku-server.com>:app-example
```

Push your changes and just wait for the magic to happens :D:

```
git push production master
```

Optional: To add SSL to the app check:
https://github.com/dokku/dokku-letsencrypt


> Further dokku configuration can be found here: http://dokku.viewdocs.io/dokku/
