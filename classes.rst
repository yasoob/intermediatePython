Classes
-------

Classes are the core of Python. They give us a lot of power but it is
really easy to misuse this power. In this section I will share some
obscure tricks and caveats related to ``classes`` in Python. Let's get
going!

1. Instance & Class variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most beginners and even some advance Python programmers do not
understand the distinction between instance and class variables. Their
lack of understanding forces them to use these different types of
variables incorrectly. Let's understand them.

The basic difference is:

-  Instance variables are for data which is unique to every object
-  Class variables are for data shared between different instances of a
   class

Let's take a look at an example:

.. code:: python

    class Cal(object):
        # pi is a class variable
        pi = 3.142

        def __init__(self, radius):
            # self.radius is an instance variable
            self.radius = radius

        def area(self):
            return self.pi * (self.radius ** 2)

    a = Cal(32)
    a.area()
    # Output: 3217.408
    a.pi
    # Output: 3.142
    a.pi = 43
    a.pi
    # Output: 43

    b = Cal(44)
    b.area()
    # Output: 6082.912
    b.pi
    # Output: 3.142
    b.pi = 50
    b.pi
    # Output: 50

There are not much issues while using mutable class variables. This is
the major reason due to which beginners do not try to learn more about
this subject because everything works! If you also believe that instance
and class variables can not cause any problem if used incorrectly then
check the next example.

.. code:: python

    class SuperClass(object):
        superpowers = []

        def __init__(self, name):
            self.name = name

        def add_superpower(self, power):
            self.superpowers.append(power)

    foo = SuperClass('foo')
    bar = SuperClass('bar')
    foo.name
    # Output: 'foo'

    bar.name
    # Output: 'bar'

    foo.add_superpower('fly')
    bar.superpowers
    # Output: ['fly']

    foo.superpowers
    # Output: ['fly']

That is the beauty of the wrong usage of mutable class variables. To
make your code safe against this kind of surprize attacks then make sure
that you do not use mutable class variables. You may use them only if
you know what you are doing.

2.New style classes:
^^^^^^^^^^^^^^^^^^^^

New style classes were introduced in Python 2.1 but a lot of people do
not know about them even now! It is so because Python also supports old
style classes just to maintain backward compatibility. I have said a lot
about new and old but I have not told you about the difference. Well the
major difference is that:

-  Old base classes do not inherit from anything
-  New style base classes inherit from ``object``

A very basic example is:

.. code:: python

    class OldClass():
        def __init__(self):
            print('I am an old class')

    class NewClass(object):
        def __init__(self):
            print('I am a jazzy new class')

    old = OldClass()
    # Output: I am an old class

    new = NewClass()
    # Output: I am a jazzy new class

This inheritance from ``object`` allows new style classes to utilize
some *magic*. A major advantage is that you can employ some useful
optimizations like ``__slots__``. You can use ``super()`` and
descriptors and the likes. Bottom line? Always try to use new-style
classes.

**Note:** Python 3 only has new-style classes. It does not matter
whether you subclass from ``object`` or not. However it is recommended
that you still subclass from ``object``.

3.Magic Methods:
^^^^^^^^^^^^^^^^

Python's classes are famous for their magic methods, commonly called
**dunder** methods. I am going to discuss a few of them.

-  ``__init__``

It is a class innitializer. Whenever an instance of a class is created
it's ``__init__`` method. For instance:

.. code:: python

    class GetTest(object):
        def __init__(self):
            print('Greetings!!')
        def another_method(self):
            print('I am another method which is not'
                  ' automatically called')

    a = GetTest()
    # Output: Greetings!!

    a.another_method()
    # Output: I am another method which is not automatically
    # called

You can see that ``__init__`` is called immediately after an instance is
created. You can also pass arguments to the class during it's
innitialization. Like this:

.. code:: python

    class GetTest(object):
        def __init__(self, name):
            print('Greetings!! {0}'.format(name))
        def another_method(self):
            print('I am another method which is not'
                  ' automatically called')

    a = GetTest('yasoob')
    # Output: Greetings!! yasoob

    # Try creating an instance without the name arguments
    b = GetTest()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: __init__() takes exactly 2 arguments (1 given)

I am sure that now you understand the ``__init__`` method.

-  ``__getitem__``

Implementing **getitem** in a class allows its instances to use the []
(indexer) operator. Here is an example:

.. code:: python

    class GetTest(object):
        def __init__(self):
            self.info = {
                'name':'Yasoob',
                'country':'Pakistan',
                'number':12345812
            }

        def __getitem__(self,i):
            return self.info[i]

    foo = OldClass()
    foo['title']
    # Output: 'Yasoob'

    foo['number']
    # Output: 36845124

Without the ``__getitem__`` method we would have got this error:

.. code:: python

    >>> foo['title']

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'GetTest' object has no attribute '__getitem__'

Static, Class & Abstract methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

