Coroutines
----------

Coroutines are similar to generators with a few differences. The main
differences are:

-  generators are data producers
-  coroutines are data consumers

First of all let's review the generator creation process. We can make
generators like this:

.. code:: python

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a+b

We then commonly use it in a ``for`` loop like this:

.. code:: python

    for i in fib():
        print(i)

It is fast and does not put a lot of pressure on memory because it
**generates** the values on the fly rather then storing them in a list.
Now if we use ``yield`` in the above example more generally we get a
coroutine. Coroutines consume values which are sent to it. A very basic
example would be a ``grep`` alternative in Python:

.. code:: python

    def grep(pattern):
        print "Searching for %s" % pattern
        while True:
            line = (yield)
            if pattern in line:
                print(line)

Wait! What does ``yield`` return? Well we have turned it into a
coroutine. It does not contain any value innitially instead we supply it
values externally. We supply values by using the ``.send()`` method.
Here is an example:

.. code:: python

    search = grep('coroutine')
    search.next()
    # Output: Searching for coroutine
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutines instead!")
    # Output: I love coroutines instead!

The sent values are accessed by yield. Why did we run ``.next()``? It is
done to start the coroutine. Just like ``generators`` coroutines do not
start the function immediately. Instead they run it in response to
``.next()`` and ``.send()`` methods. Therefore you have to run
``.next()`` so that the execution advances to the ``yield`` expression.

We can close a coroutine by calling the ``.close()`` method. Like:

.. code:: python

    search = grep('coroutine')
    # ...
    search.close()

There is a lot more to ``coroutines``. I suggest you check out `this
awesome
presentation <http://www.dabeaz.com/coroutines/Coroutines.pdf>`__ by
David Beazley.
