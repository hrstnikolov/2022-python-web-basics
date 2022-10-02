# Steps

Project
- `petstagram`
- run server to verify
- delete Django comments

Apps
- `photos`, `pets`, `accounts`, and `common`
- move the apps inside the project folder
- register apps in settings.py

URLs
- create app URLs (empty tuple)
- include in project URLs
- the home page is `common`

Templates
- divide all templates in separate directories
- folder names are the same as app names

Views
- add views that return rendered template
- pay attention to the naming in the `account`  app
- create URLs to access each view

Static files
- Create a new folder `staticfiles`
- Copy the exiting html and CSS







Navigation
Separate the navigation in a partial template

templates

Replace all absolute paths with static tag

update the nav urls

template inheritence

replace homepage div class=card -> for loop and create partial template

nginx

py managepy runserver --insecure

STATIC_ROOT = "tmp/petstagram/static-files"

py managepy collectstatic -> copies the file