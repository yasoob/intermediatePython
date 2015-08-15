Map & Filter
------------

These are two functions which facilitate a functional approach to
programming. We will discuss them one by one and understand their use
cases.

1. Map
^^^^^^

``Map`` applies a function to all the items in an input\_list. Here is
the blueprint:

**Blueprint**

.. code:: python

    map(functions_to_apply, list_of_inputs)

Most of the times we want to pass all the list elements to a function
one-by-one and then collect the output. For instance:

.. code:: python

    items = [1, 2, 3, 4, 5]
    squared = []
    for i in items:
        squared.append(i**2)

``Map`` allows us to implement this in a much simpler and nicer way.
Here you go:

.. code:: python

    items = [1, 2, 3, 4, 5]
    squared = map(lambda x: x**2, items)

Most of the times we use lambdas with ``map`` so I did the same. Instead
of a list of inputs we can even have a list of functions!

.. code:: python

    def multiply(x):
            return (x*x)
    def add(x):
            return (x+x)

    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print(value)
        
    # Output:
    # [0, 0]
    # [1, 2]
    # [4, 4]
    # [9, 6]
    # [16, 8]

2. Filter
^^^^^^^^^

As the name suggests, filter creats a list of elements for which a
function returns true. Here is a short and consise example:

.. code:: python

    number_list = range(-5,5)
    less_than_zero = list(filter(lambda x: x<0, number_list))
    print(less_than_zero)

    # Output: [-5, -4, -3, -2, -1]

The filter resembles a for loop but it is a builtin function and faster.

**Note:** If map & filter do not appear beautiful to you then you can
read about ``list/dict/tuple`` comprehensions.
