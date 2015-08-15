For - Else
----------

Loops are an integral part of any language. Likewise ``for`` loops are
an important part of Python. However there are a few things which most
beginners do not know about them. We will discuss a few of them one by
one.

Let's first start of by what we know. We know that we can use for loops
like this:

::

    fruits = ['apple', 'banana', 'mango']
    for fruit in fruits:
        print fruit.capitalize()

    # Output: Apple
    #         Banana
    #         Mango

That is the very basic structure of a for loop. Now let's move on to
some of the lesser known features of ``for`` loops in Python.

1.\ ``else`` clause:
^^^^^^^^^^^^^^^^^^^^

For loops also have an ``else`` clause which most of us are unfamiliar
with. The ``else`` clause executes when the loop completes normally.
This means that the loop did not encounter any ``break``. They are
really useful once you understand where to use them. I myself came to
know about them a lot later.

The common construct is to run a loop and search for an item. If the
item is found, we break the loop using ``break``. There are two
scenarios in which the loop may end. The first one is when the item is
found and ``break`` is encountered. The second scenario is that the loop
ends. Now we may want to know which one of these is the reason for a
loops completion. One method is to set a flag and then check it once the
loop ends. Another is to use the ``else`` clause.

This is the basic structure of a ``for/else`` loop:

.. code:: python

    for item in container:
        if search_comething(item):
            # Found it!
            process(item)
            break
    else:
        # Didn't find anything..
        not_found_in_container()

Consider this simple example which I took from the official
documentation:

.. code:: python

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break

It outputs the prime numbers between 2 to 10. Now for the fun part. We
can add an additional ``else`` block which catches the numbers which are
not prime and tells us so:

::

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break
        else:
            # loop fell through without finding a factor
            print n, 'is a prime number'

