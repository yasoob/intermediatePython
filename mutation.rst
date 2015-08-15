Mutation
--------

The mutable and immutable datatypes in Python cause a lot of headache
for new programmers. In simple words, mutable means 'able to be changed'
and immutable means 'constant'. Want your head to spin? Consider this
example:

.. code:: python

    foo = ['hi']
    print(foo)
    # Output: ['hi']

    bar = foo
    bar += ['bye']
    print(foo)
    # Output: ['hi', 'bye']

What just happened? We were not expecting that! We were expecting
something like this:

.. code:: python

    foo = ['hi']
    print(foo)
    # Output: ['hi']

    bar = foo
    bar += ['bye']

    print(foo)
    # Output: ['hi']

    print(bar)
    # Output: ['hi', 'bye']

It's not a bug. It's mutability in action. Whenever you assign a
variable to another variable of mutable datatype, any changes to the
data are reflected by both variables. The new variable is just an alias
for the old variable. This is only true for mutable datatypes. Here is a
gotcha involving functions and mutable data types:

.. code:: python

    def add_to(num, target=[]):
        target.append(num)
        return target

    add_to(1)
    # Output: [1]

    add_to(2)
    # Output: [1, 2]

    add_to(3)
    # Output: [1, 2, 3]

You might have expected it to behave differently. You might be expecting
that a fresh list would be created when you call ``add_to`` like this:

.. code:: python

    def add_to(num, target=[]):
        target.append(num)
        return target

    add_to(1)
    # Output: [1]

    add_to(2)
    # Output: [2]

    add_to(3)
    # Output: [3]

Well again it is the mutability of lists which causes this pain. In
Python the default arguments are evaluated once when the function is
defined, not each time the function is called. You should never define
default arguments of mutable type unless you know what you are doing.
You should do something like this:

.. code:: python

    def add_to(element, target=None):
        if target is None:
            target = []
        target.append(element)
        return target

Now whenever you call the function without the ``target`` argument, a
new list is created. For instance:

.. code:: python

    add_to(42)
    # Output: [42]

    add_to(42)
    # Output: [42]

    add_to(42)
    # Output: [42]

