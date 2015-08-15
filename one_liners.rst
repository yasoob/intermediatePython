One Liners
----------

In this chapter I will show you some one liner Python commands which can
be really helpful sometimes.

**Simple Webserver**

Ever wanted to quickly share a file over a network? Well you are in
luck. Python has a similar feature just for you. Go to the directory
which you want to serve over network and write the following code in
terminal:

.. code:: python

    # Python 2
    python -m SimpleHTTPServer

    # Python 3
    python -m http.server

**Pretty printing**

You can print a list and dictionary in a beautiful format in Python
repl. Here is the relevant code:

.. code:: python

    from pprint import pprint

    my_dict = {'name':'Yasoob',
    'age':'undefined','personality':'awesome'}
    pprint(my_dict)

This is more effective on dicts. Moreover, if you want to pretty print
json quickly from a file then you can simply do:

.. code:: python

    cat file.json | python -m json.tools

**Profiling a script**

This can be extremely helpful in pin pointing the bottlenecks in your
scripts.

.. code:: python

    python -m cProfile my_script.py

Note: ``cProfile`` is a faster implementation of ``profile`` as it is
written in c

**CSV to json**

Run this in the terminal:

.. code:: python

    python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

Make sure that you replace ``csv_file.csv`` to the relevant file name.

**List Flattening**

You can quickly and easily flatten a list using
``itertools.chain.from_iterable`` from the ``itertools`` package. Here
is a simple example:

.. code:: python

    a_list = [[1, 2], [3, 4], [5, 6]]
    print(list(itertools.chain.from_iterable(a_list)))
    # Output: [1, 2, 3, 4, 5, 6]

A couple of more one liners can be found on the `Python
website <https://wiki.python.org/moin/Powerful%20Python%20One-Liners>`__
