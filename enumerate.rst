Enumerate
---------

Enumerate is a built-in function of Python. It's usefulness can not be
summarized in a single line. Yet most of the newcommers and even some
advanced programmers are unaware of it. It allows us to loop over
something and have an automatic counter. Here is an example:

.. code:: python

    for counter, value in enumerate(some_list):
        print(counter, value)

This is not it. ``enumerate`` also accepts some optional arguments which
make it even more useful.

.. code:: python

    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)

    # Output:
    # 1 apple
    # 2 banana
    # 3 grapes
    # 4 pear

The optional argument allows us to tell ``enumerate`` from where to
start the index. You can also create tuples containing the index and
list item using a list. Here is an example:

.. code:: python

    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list,1))
    print(counter_list)
    # Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]

