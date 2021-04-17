One-Liners
----------

In this chapter I will show you some one-liner Python commands which can
be really helpful.

**Simple Web Server**

Ever wanted to quickly share a file over a network? Well you are in
luck. Python has a feature just for you. Go to the directory
which you want to serve over the network and write the following code in
your terminal:

.. code:: python

    # Python 2
    python -m SimpleHTTPServer

    # Python 3
    python -m http.server

**Pretty Printing**

You can print a list and dictionary in a beautiful format in the Python
repl. Here is the relevant code:

.. code:: python

    from pprint import pprint

    my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
    print(dir(my_dict))
    # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    
    print(dir(my_dict))
    # ['__add__',
    #  '__class__',
    #  '__contains__',
    #  '__delattr__',
    #  '__delitem__',
    #  '__dir__',
    #  '__doc__',
    #  '__eq__',
    #  '__format__',
    #  '__ge__',
    #  '__getattribute__',
    #  '__getitem__',
    #  '__gt__',
    #  '__hash__',
    #  '__iadd__',
    #  '__imul__',
    #  '__init__',
    #  '__init_subclass__',
    #  '__iter__',
    #  '__le__',
    #  '__len__',
    #  '__lt__',
    #  '__mul__',
    #  '__ne__',
    #  '__new__',
    #  '__reduce__',
    #  '__reduce_ex__',
    #  '__repr__',
    #  '__reversed__',
    #  '__rmul__',
    #  '__setattr__',
    #  '__setitem__',
    #  '__sizeof__',
    #  '__str__',
    #  '__subclasshook__',
    #  'append',
    #  'clear',
    #  'copy',
    #  'count',
    #  'extend',
    #  'index',
    #  'insert',
    #  'pop',
    #  'remove',
    #  'reverse',
    #  'sort']


This is more effective on nested ``dict`` s. Moreover, if you want to pretty print
json quickly from a file then you can simply do:

.. code:: python

    cat file.json | python -m json.tool

**Profiling a script**

This can be extremely helpful in pinpointing the bottlenecks in your
scripts:

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
    
    # or 
    print(list(itertools.chain(*a_list)))
    # Output: [1, 2, 3, 4, 5, 6]


**One-Line Constructors**

Avoid a lot of boilerplate assignments when initializing a class

.. code:: python

    class A(object):
        def __init__(self, a, b, c, d, e, f):
            self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


Additional one-liners can be found on the `Python
website <https://wiki.python.org/moin/Powerful%20Python%20One-Liners>`__.
