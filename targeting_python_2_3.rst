Targeting Python 2+3
--------------------

In a lot of cases you might want to develop programs which can be run in
both Python 2+ and 3+.

Just imagine that you have a very popular Python module which is used by
hundreds of people but not all of them have Python 2 or 3. In that case
you have two choices. The first one is to distribute 2 modules, one for
Python 2 and the other for Python 3. The other choice is to modify your
current code and make it compatible with both Python 2 and 3.

In this section I am going to highlight some of the tricks which you can
employ to make a script compatible with both of them.

**Future imports**

The first and most important method is to use ``__future__`` imports. It
allows you to import Python 3 functionality in Python 2. Here are a couple
examples:

Context managers were new in Python 2.6+. For using them in Python 2.5 you can use:

.. code:: python

    from __future__ import with_statement

``print`` was changed to a function in Python 3. If you want to use it
in Python 2 you can import it from ``__future__``:

.. code:: python

    print
    # Output:

    from __future__ import print_function
    print(print)
    # Output: <built-in function print>

**Dealing with module renaming**

First, tell me how you import packages in your script ? Most of us do
this :

.. code:: python

    import foo
    # or
    from foo import bar

Do you know that you can do something like this as well?

.. code:: python

    import foo as foo

I know its function is the same as the above listed code but it is vital
for making your script compatible with Python 2 and 3. Now examine the
code below :

.. code:: python

    try:
        import urllib.request as urllib_request  # for Python 3
    except ImportError:
        import urllib2 as urllib_request  # for Python 2

So let me explain the above code a little. We are wrapping our importing
code in a ``try/except`` clause. We are doing it because in Python 2 there is
no ``urllib.request`` module so this would result in an ``ImportError``. The
functionality of ``urllib.request`` is provided by the ``urllib2`` module in
Python 2. So, when using Python 2, we try to import ``urllib.request`` and
if we get an ``ImportError`` then we tell Python to import ``urllib2`` instead.

The final thing you need to know about is the ``as`` keyword. It is
mapping the imported module to ``urllib_request``. So that all of
the classes and methods within ``urllib2`` are available to us via the alias
``urllib_request``.

**Obsolete Python 2 builtins**

Another thing to keep in mind is that there are 12 Python 2 builtins
which have been removed from Python 3. Make sure that you don't use them
in Python 2 in order to make your code compatible with Python 3.
Here is a way to enforce that you abandon these 12 builtins in Python 2 as
well:

.. code:: python

    from future.builtins.disabled import *

Now whenever you try to use the modules which are abandoned in Python 3,
it raises a ``NameError`` like this:

.. code:: python

    from future.builtins.disabled import *

    apply()
    # Output: NameError: obsolete Python 2 builtin apply is disabled

**External standard-library backports**

There are a few packages in the wild which provide Python 3
functionality in Python 2. For instance, we have:

-  enum ``pip install enum34``
-  singledispatch ``pip install singledispatch``
-  pathlib ``pip install pathlib``

For further reading, the Python documentation has a `comprehensive guide
<https://docs.python.org/3/howto/pyporting.html>`_ of steps you need to
take to make your code compatible with both Python 2 and 3.
