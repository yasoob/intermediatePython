Ternary Operators
-----------------

Ternary operators are more commonly known as conditional expressions in
Python. These operators evaluate something based on a condition being
true or not. They became a part of Python in version 2.4

Here is a blueprint and an example of using these conditional
expressions.

**Blueprint:**

.. code:: python

    condition_if_true if condition else condition_if_false

**Example:**

.. code:: python

    is_nice = True
    state = "nice" if is_nice else "not nice"

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

    nice = True
    personality = ("mean", "nice")[nice]
    print("The cat is ", personality)
    # Output: The cat is nice

This works simply because True == 1 and False == 0, and so can be done
with lists in addition to tuples.

The above example is not widely used and is generally disliked by
Pythonistas for not being Pythonic. It is also easy to confuse where to
put the true value and where to put the false value in the tuple.

Another reason to avoid using a tupled ternery is that it results in
both elements of the tuple being evaluated, whereas the if-else
ternary operator does not.

**Example:**

.. code:: python

    condition = True
    print(2 if condition else 1/0)
    #Output is 2

    print((1/0, 2)[condition])
    #ZeroDivisionError is raised
    
This happens because with the tupled ternary technique, the tuple is
first built, then an index is found.  For the if-else ternary operator,
it follows the normal if-else logic tree.  Thus, if one case could
raise an exception based on the condition, or if either case is a
computation-heavy method, using tuples is best avoided.


**ShortHand Ternary**

In python there is also the shorthand ternary tag which is a shorter version of the 
normal ternary operator you have seen above. 

Syntax was introduced in Python 2.5 and can be used in python 2.5 or greater.

**Example**

.. code:: python

    >>> True or "Some"
    True
    >>>
    >>> False or "Some"
    'Some'

The first statement (`True or "Some"`) will return `True` and the second statement (`False or "Some"`) will return `Some`. 

This is helpful in case where you quickly want to check for the output of a function and give a useful message if the output is empty:

.. code:: python

    >>> func_output = None
    >>> msg = output or "No data returned"
    >>> print(msg)
    No data returned


