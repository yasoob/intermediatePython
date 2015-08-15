Global & Return
---------------

You might have encountered some functions written in python which have a
return keyword in the end of the function. Do you know what it does ? It
is similar to return in other languages. Lets examine this little
function:

.. code:: python

    def add(value1,value2):
        return value1 + value2

    result = add(3,5)
    print(result)
    # Output: 8

The function above takes two values as input and then output their
addition. We could have also done:

.. code:: python

    def add(value1,value2):
        global result
        result = value1 + value2

    add(3,5)
    print(result)
    # Output: 8

So first lets talk about the first bit of code which involves the
``return`` keyword. What that function is doing is that it is assigning
the value to the variable which is calling that function which in our
case is ``result``. In most cases and you won't need to use the
``global`` keyword. However lets examine the other bit of code as well
which includes the ``global`` keyword. So what that function is doing is
that it is making a global variable ``result``. What does global mean
here? Global variable means that we can access that variable outside the
scope of the function as well. Let me demonstrate it with an example :

.. code:: python

    # first without the global variable
    def add(value1,value2):
        result = value1 + value2

    add(2,4)
    print(result)

    # Oh crap we encountered an exception. Why is it so ?
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
    def add(value1,value2):
        global result
        result = value1 + value2

    add(2,4)
    result
    6

So hopefully there are no errors in the second run as expected. In
practical programming you should try to stay away from ``global``
keyword as it only makes life difficult by introducing unwated variables
to the global scope.
