Lambdas
-------

Lambdas are one line functions. They are also known as anonymous
functions in some other languages. You might want to use lambdas when
you don't want to use a function twice in a program. They are just like
normal functions and even behave like them.

**Blueprint**

.. code:: python

    lambda argument: manipulate(argument)

**Example**

.. code:: python

    add = lambda x,y: x+y

    print(add(3,5))
    # Output: 8

Here are a few useful use cases for lambdas and just a few way in which
they are used in the wild:

**List sorting**

.. code:: python

    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1])

    print(a)
    # Output: [(13, -3), (4, 1), (1, 2), (9, 10)] 

**Parallel sorting of lists**

.. code:: python

    data = zip(list1, list2)
    data.sort()
    list1, list2 = map(lambda t: list(t), zip(*data))

Note: We will learn about map in a later chapter so don't worry!
