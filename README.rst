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
