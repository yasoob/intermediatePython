Ternary Operators
-----------------

Ternary operators are more commonly known as conditional expressions in
Python. These operators evaluate something based on a condition being
true or not. They became a part of Python in version 2.4

Here is a blueprint and an example of using these conditional
expressions.

**Blueprint:**

.. code:: python

    condition_is_true if condition_true else condition_is_false

**Example:**

.. code:: python

    is_fat = True
    state = "fat" if is_fat else "not fat"

It allows to quickly test a condition instead of a multiline if
statement. Often times it can be immensely helpful and can make your
code compact but still maintainable.

Another more obscure and not widely used example involves tuples. Here
is some sample code:

**Blueprint:**

.. code:: python

    (if_test_is_false, if_test_is_true)[test]

**Example:**

.. code:: python

    fat = True
    fitness = ("skinny","fat")[fat]
    print("Ali is " + fitness)
    # Output: Ali is fat

The above example is not widely used and is generally disliked by
Pythonistas for not being Pythonic. It is also easy to confuse where to
put the true value and where to put the false value in the tuple.
