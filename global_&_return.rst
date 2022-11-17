Global and Return
---------------

You might have encountered some functions written in Python which have a
``return`` keyword in the end of the function. Do you know what it does? It
is similar to return in other languages. Let's examine this little
function:

.. code:: python

    def add(value1, value2):
        return value1 + value2

    result = add(3, 5)
    print(result)
    # Output: 8

The function above takes two values as input and then outputs their
addition. We could have also done:

.. code:: python

    def add(value1,value2):
        global result
        result = value1 + value2

    add(3,5)
    print(result)
    # Output: 8

So first let's talk about the first bit of code which involves the
``return`` keyword. What that function is doing is that it is assigning
the value to the variable which is calling that function which in our
case is ``result``. In most cases you won't need to use the
``global`` keyword. However, let's examine the other bit of code as well
which includes the ``global`` keyword. So what that function is doing is
that it is making a global variable ``result``. What does global mean
here? Global variable means that we can access that variable outside the
scope of the function as well. Let me demonstrate it with an example:

.. code:: python

    # first without the global variable
    def add(value1, value2):
        result = value1 + value2

    add(2, 4)
    print(result)

    # Oh crap, we encountered an exception. Why is it so?
    # the python interpreter is telling us that we do not
    # have any variable with the name of result. It is so
    # because the result variable is only accessible inside
    # the function in which it is created if it is not global.
    Traceback (most recent call last):
      File "", line 1, in
        result
    NameError: name 'result' is not defined

    # Now lets run the same code but after making the result
    # variable global
    def add(value1, value2):
        global result
        result = value1 + value2

    add(2, 4)
    result
    6

So hopefully there are no errors in the second run as expected. In
practical programming you should try to stay away from ``global``
keyword as it only makes life difficult by introducing unwanted variables
to the global scope.

Multiple return values
^^^^^^^^^^^^^^^^^^^^^^^

So what if you want to return two variables from a function instead of one? There are a couple of approaches which new programmers take. The most famous approach is to use ``global`` keyword. Let's take a look at a useless example:

.. code:: python

    def profile():
        global name
        global age
        name = "Danny"
        age = 30

    profile()
    print(name)
    # Output: Danny

    print(age)
    # Output: 30

**Note:**Don't try to use the above mentioned method. I repeat, don't try to use the above mentioned method!

Some try to solve this problem by *returning* a ``tuple``, ``list`` or ``dict`` with the required values after the function terminates. It is one way to do it and works like a charm:

.. code:: python

    def profile():
        name = "Danny"
        age = 30
        return (name, age)

    profile_data = profile()
    print(profile_data[0])
    # Output: Danny

    print(profile_data[1])
    # Output: 30

Or by more common convention:

.. code:: python

    def profile():
        name = "Danny"
        age = 30
        return name, age

    profile_name, profile_age = profile()
    print(profile_name)
    # Output: Danny
    print(profile_age)
    # Output: 30

Keep in mind that even in the above example we are returning a tuple (despite the lack of parenthesis) and not separate multiple values. If you want to take it one step further, you can also make use of `namedtuple <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_. Here is an example:

.. code:: python

    from collections import namedtuple
    def profile():
        Person = namedtuple('Person', 'name age')
        return Person(name="Danny", age=31)

    # Use as namedtuple
    p = profile()
    print(p, type(p))
    # Person(name='Danny', age=31) <class '__main__.Person'>
    print(p.name)
    # Danny
    print(p.age)
    #31

    # Use as plain tuple
    p = profile()
    print(p[0])
    # Danny
    print(p[1])
    #31

    # Unpack it immediatly
    name, age = profile()
    print(name)
    # Danny
    print(age)
    #31

This is a better way to do it, along with returning ``list`` and ``dict``. Don't use ``global`` keyword unless you know what you are doing. ``global`` might be a better option in a few cases but is not in most of them.
