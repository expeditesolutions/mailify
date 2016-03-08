This is the sourcecode for the mailify website.


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


Lockout
-------

This website uses django-axes to prevent brute-forcing the login system.
Default it will lock an user out by attempting 5 times the wrong username/password combination (not unique per browser).
It will then show the template defined in settings.AXES_LOCKOUT_TEMPLATE.
The user will be able to login again after settings.AXES_COOLOFF_TIME.

In case you lock yourself out, you can remove the logged attempts here:::

    $ python manage.py axes_reset

The attempts can also manually be removed from the django-admin. That is, if it's not you who has been locked out :)


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
