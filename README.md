milk
====

RESTful ascii cows using Flask

really?
-------

Consider this a Flask "hello world"

dependencies
------------

 - [Flask](https://github.com/mitsuhiko/flask.git)
 - [cowsay](https://github.com/schacon/cowsay)

using
-----

Launch a Flask with all the defaults:

    ./milk.py

Then curl away:

    curl -X GET http://localhost:5000/cow/say?message=moo

future
------

 - Support for cowthink
 - Support for different types of cow.
