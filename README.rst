This is the sourcecode for the mailify website.

Prerequisites
=============

Production
----------

- Python 3.5.1  (noted in runtime.txt)
- PostgreSQL 9.4 (or higher)
- Python packages found in requirements.txt

Development
-----------
- Git
- Python 3.5.1  (noted in runtime.txt)
- PostgreSQL 9.4 (or higher)
- Virtualenvwrapper (https://virtualenvwrapper.readthedocs.org/en/latest/)
  This is a tool that lets you install python packages in a virtualenv, meaning
  you can have multiple projects on your computer with different versions
  of packages without them interfering with eachother.
- Python packages found in requirements.txt
- Python packages for testing in requirements-testing.txt
- Heroku toolbelt, to be able to deploy to Heroku from command


Installation
============

Installation (local)
--------------------

::

    $ git clone git@github.com:Webdesignwill/mailify.git mailify
    $ cd mailify
    $ pip install -r requirements.txt

    Now copy mailify/local_example.py to mailify/local.py and fill in the database credentials.

::

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver


Deployment
----------
This website currently uses a Heroku setup.
To deploy with Heroku, you first need the Heroku Toolbelt:

https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Then I suggest you cd into the project root, and login to Heroku::

    $ heroku login

When that's done, you should use the following command to deploy::

    $ deploy/deploy_production.sh

This will push the current branch to heroku master, and run the database
migrations (if needed) and finally openup the server in your browser.


Lockout
-------

This website uses django-axes to prevent brute-forcing the login system.
Default it will lock an user out by attempting 5 times the wrong username/password combination (not unique per browser).
It will then show the template defined in settings.AXES_LOCKOUT_TEMPLATE.
The user will be able to login again after settings.AXES_COOLOFF_TIME.

In case you lock yourself out, you can remove the logged attempts here:::

    $ python manage.py axes_reset

The attempts can also manually be removed from the django-admin. That is, if it's not you who has been locked out.


Testing
-------

::

    $ pip install -r ./requirements-testing.txt
    $ py.test


PEP8
----

To validate all Python code according to the PEP8 standards:

::

    $ pip install -r ./requirements-testing.txt
    $ ./src/linter.sh


Coverage
--------

To get an overview on how much the tests cover the project, you can use coverage.
Warning: 100% coverage doesn't mean 100% branch-coverage. Even 100% branch-coverage
is no guaruantee that everything is tested. This is not possible.
See coverage as a guideline to make tests.

::

    $ cd src
    $ coverage run --source . -m py.test && coverage html
