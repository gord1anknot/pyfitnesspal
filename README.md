# PyFitnessPal

*a simple [myfitnesspal](http://www.myfitnesspal.com/) clone made with [django](https://www.djangoproject.com/)*

## Motivation

MyFitnessPal makes it very easy to enter data, with a very large database and multiple apps (web, iOS, Android). However, it's not so easy to get reports or data out of it. There's only one [highcharts](.make_secret.py) based line graph, and no click-to-export anywhere.

PyFitnessPal doesn't have the features for input or sharing of data with other users, but is _planned_ to be more extensible in the data importing, reporting and exporting departments.

Features To Add:

- ~~CRUD Food Item~~
- ~~CRUD Daily Log Item~~
- Report
- CRUD Users
- CRUD per-user Daily Log Item
- Tests
- CI
- Heroku Deploy Button

## Deploy on Heroku

You can deploy directly to Heroku with the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

After deploying, run the Django `migrate` command to initialize your postgres database, and run the Django `syncdb` command to set up the root administrator account:

```
$ heroku clone -a new-app-name
$ heroku run python manage.py migrate
$ heroku run python manage.py syncdb
```

Once you've deployed, you can easily clone the app and make modifications:

```
$ heroku clone -a new-app-name
...
$ vim templates/login.html
$ git add .
$ git commit -m "updating login view"
$ git push heroku master
...
```

## Running Locally

Install [Python](https://www.python.org/) 2.7.9 locally, and create and activate a virutalenv using the `create_venv.sh` shell script:

```
brew install python
pip install virtualenv
./create_venv.sh
. .venv/bin/activate
```

You must use the [twelve-factor approved method](https://devcenter.heroku.com/articles/getting-started-with-django#django-settings) to specify your database connection url.

As an example, if you want the Django, vanilla [sqlite](https://sqlite.org/) setup, set the `DATABASE_URL` environment variable before doing anything with `manage.py`:

```
export DATABASE_URL=sqlite:///$(pwd)/db.sqlite3
```

an sqlite backend can also be run in memory:

```
export DATABASE_URL=sqlite://:memory:
```

Use [`honcho`](https://honcho.readthedocs.org/en/latest/) to start the application with [gunicorn](http://gunicorn.org), pretty much like Heroku does:

```
cat>>.env<<EOF
DATABASE_URL="sqlite:///$(pwd)/db.sqlite3"
SECRET_KEY="$(./.make_secret.py)
EOF
.venv/bin/honcho start
```

Immediately after the initial start, you must run the migration to set up your new database.

```
./.venv/bin/python manage.py migrate
```

Set up an initial administrator account with the `syncdb` command:

```
./.venv/bin/python manage.py syncdb
```