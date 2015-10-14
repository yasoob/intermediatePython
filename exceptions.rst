Exceptions
----------

Exception handling is an art which once you master grants you immense
powers. I am going to show you some of the ways in which we can handle
exceptions.

In basic terminology we are aware of ``try/except`` clause. The code
which can cause an exception to occur is put in the ``try`` block and
the handling of the exception is implemented in the ``except`` block.
Here is a simple example:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except IOError as e:
        print('An IOError occurred. {}'.format(e.args[-1]))

In the above example we are handling only the IOError exception. What
most beginners do not know is that we can handle multiple exceptions.

Handling multiple exceptions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can use three methods to handle multiple exceptions. The first one
involves putting all the exceptions which are likely to occur in a
tuple. Like so:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except (IOError, EOFError) as e:
        print("An error occurred. {}".format(e.args[-1]))

Another method is to handle individual exceptions in separate ``except``
blocks. We can have as many ``except`` blocks as we want. Here is an example:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except EOFError as e:
        print("An EOF error occurred.")
        raise e
    except IOError as e:
        print("An error occurred.")
        raise e

This way if the exception is not handled by the first ``except`` block then
it may be handled by a following block, or none at all. Now the last method involves
trapping ALL exceptions:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except Exception:
        # Some logging if you want
        raise

This can be helpful when you have no idea about the exceptions which may
be thrown by your program.

``finally`` clause
~~~~~~~~~~~~~~~~~~

We wrap our main code in the ``try`` clause. After that we wrap some code in
an ``except`` clause which gets executed if an exception occurs in the code
wrapped in the ``try`` clause. In this example we will use a third clause as
well which is the ``finally`` clause. The code which is wrapped in the
``finally`` clause will run whether or not an exception occurred. It might be used
to perform clean-up after a script. Here is a simple example:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except IOError as e:
        print('An IOError occurred. {}'.format(e.args[-1]))
    finally:
        print("This would be printed whether or not an exception occurred!")
        
    # Output: An IOError occurred. No such file or directory
    # This would be printed whether or not an exception occurred!

``try/else`` clause
~~~~~~~~~~~~~~~~~~~

Often times we might want some code to run if **no** exception occurs. This
can easily be achieved by using an ``else`` clause. One might ask: why, if
you only want some code to run if no exception occurs, wouldn't you simply
put that code inside the ``try``? The answer is that then any exceptions in
that code will be caught by the ``try``, and you might not want that. Most
people don't use it and honestly I have myself not used it widely. Here is an
example:

.. code:: python

    try:
        print('I am sure no exception is going to occur!')
    except Exception:
        print('exception')
    else:
        # any code that should only run if no exception occurs in the try,
        # but for which exceptions should NOT be caught
        print('This would only run if no exception occurs. And an error here '
              'would NOT be caught.')
    finally:
        print('This would be printed in every case.')

    # Output: I am sure no exception is going to occur!
    # This would only run if no exception occurs.
    # This would be printed in every case.

The ``else`` clause would only run if no exception occurs and it would run
before the ``finally`` clause.
