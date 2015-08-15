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
        file = open('test.txt','rb')
    except IOError as e:
        print('An IOError occured. {}'.format(e.args[-1]))

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
    except (IOError,EOFError) as e:
        print("An error occured. {}".format(e.args[-1]))

Another method is to handle individual exception in a separate except
block. We can have as many except blocks as we want. Here is an example:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except EOFError as e:
        print("An EOF error occured.")
        raise e
    except IOError as e:
        print("An error occured.")
        raise e

This way if the exception is not handled by the first except block then
it is passed on to the second block. Now the last method involves
traping ALL exceptions:

.. code:: python

    try:
        file = open('test.txt', 'rb')
    except:
        # Some loggin if you want
        raise

This can be helpful when you have no idea about the exception which can
be thrown by your program.

``Finally`` caluse
~~~~~~~~~~~~~~~~~~

We wrap our main code in the try clause. After that we wrap some code in
except clause which gets executed if an exception occurs in the code
wrapped in try clause. But in this example we will use a third clause as
well which is the ``finally`` clause. The code which is wrapped in the
finally clause will run even if no exception occurs. It might be used
for cleaning up after a script. Here is a simple example:

.. code:: python

    try:
        file = open('test.txt','rb')
    except IOError as e:
        print('An IOError occured. {}'.format(e.args[-1]))
    finally:
        print("This would be printed even if no exception occurs!")
        
    # Output: An IOError occured. No such file or directory
    # This would be printed even if no exception occurs!

``try/else`` clause
~~~~~~~~~~~~~~~~~~~

Often times we might want some code to run IF no exception occurs. This
can easily be achieved by using an ``else`` clause. Most people don't
use it and honestly I have myself not used it widely. Here is an
example:

.. code:: python

    try:
        print('I am sure no exception is going to occur!')
    except:
        print("exception")
    else:
        print('This would only run if no exception occurs.')
    finally:
        print("This would be printed in every case.")

    # Output: I am sure no exception is going to occur!
    # This would only run if no exception occurs.
    # This would be printed in every case.

The else clause would only run if no exception occurs and it would run
before the ``finally`` clause.
