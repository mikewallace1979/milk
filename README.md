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

You can also make the cow think:

    curl -X GET http://localhost:5000/cow/think?message=moo

And use any of the cowfiles provided by cowsay:

    curl -X GET http://localhost:5000/cow/say?message=moo\&cowfile=stimpy

A list of supported values for cowfile can be obtained using:

    curl -X GET http://localhost:5000/cows
