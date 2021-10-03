Food Recommender System
======

Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::

    # clone the repository
    $ git clone https://github.com/iravikds/food-recommender-system
    $ cd food-recommender-system

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat


Run
---

::

    $ export FLASK_APP=food-recommender-system
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=food-recommender-system
    > flask run

Open http://127.0.0.1:5000 in a browser.

