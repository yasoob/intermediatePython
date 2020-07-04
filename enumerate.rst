Enumerate
---------

Enumerate is a built-in function of Python. Its usefulness can not be
summarized in a single line. Yet most of the newcomers and even some
advanced programmers are unaware of it. It allows us to loop over
something and have an automatic counter. Here is an example:

.. code:: python
    
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for counter, value in enumerate(my_list):
        print counter, value

    # Output:
    # 0 apple
    # 1 banana
    # 2 grapes
    # 3 pear

And there is more! ``enumerate`` also accepts an optional argument that
allows us to specify the starting index of the counter.

.. code:: python

    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)

    # Output:
    # 1 apple
    # 2 banana
    # 3 grapes
    # 4 pear

An example of where the optional argument of ``enumerate``comes in handy
is creating tuples containing the index and list item using a list. Here 
is an example:

.. code:: python

    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list, 1))
    print(counter_list)
    # Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]

