Enumerate
---------

Enumerate is a built-in function of Python. Its usefulness can not be
summarized in a single line. Yet most of the newcomers and even some
advanced programmers are unaware of it. It allows us to loop over
something and have an automatic counter. Here is an example:

.. code:: python

    for counter, value in enumerate(some_list):
        print(counter, value)

And there is more! ``enumerate`` also accepts an optional argument which
makes it even more useful.

.. code:: python

    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)

    # Output:
    # 0 apple
    # 1 banana
    # 2 grapes
    # 3 pear

The optional argument allows us to tell ``enumerate`` from where to
start the index. You can also create tuples containing the index and
list item using a list. Here is an example:

.. code:: python

    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list, 1))
    print(counter_list)
    # Output: [(0, 'apple'), (1, 'banana'), (2, 'grapes'), (3, 'pear')]

