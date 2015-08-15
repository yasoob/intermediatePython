Decorators
----------

Decorators are a significant part of Python. In simple words they are
functions which modify the functionality of another function. They help
to make our code shorter and more Pythonic. Most of the beginners do not
know where to use them so I am going to share some areas where
decorators can make your code consise.

Firstly let's discuss how to write your own decorator.

It is perhaps one of the most difficult concept to grasp. We will take
it one step at a time so that you can fully inderstand it.

Everything in python is an object:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First of all let's understand functions in python:

::

    def hi(name="yasoob"):
        return "hi "+name

    print hi()
    #output: 'hi yasoob'

    #We can even assign a function to a variable like
    greet = hi
    #We are not using parentheses here because we are not calling the function hi
    #instead we are just putting it into the greet variable. Let's try to run this

    print greet()
    #output: 'hi yasoob'

    #lets see what happens if we delete the old hi function!
    del hi
    print hi()
    #outputs: NameError

    print greet()
    #outputs: 'hi yasoob'

Defining functions within functions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So those are the basics when it comes to functions. Lets take your
knowledge one step further. In Python we can define functions inside
other functions:

::

    def hi(name="yasoob"):
        print "now you are inside the hi() function"

        def greet():
            return "now you are in the greet() function"

        def welcome():
            return "now you are in the welcome() function"

        print greet()
        print welcome()
        print "now you are back in the hi() function"

    hi()
    #output:now you are inside the hi() function
    #       now you are in the greet() function
    #       now you are in the welcome() function
    #       now you are back in the hi() function

    # This shows that whenever you call hi(), greet() and welcome()
    # are also called. However the greet() and welcome() functions
    # are not available outsite the hi() function e.g:

    greet()
    #outputs: NameError: name 'greet' is not defined

So now we know that we can define functions in other functions. In
simpler words we can make nested functions. Now you need to learn one
more thing that functions can return functions too.

Returning functions from within functions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is not necessary to execute a function within another function, we
can return it as an output as well:

::

    def hi(name="yasoob"):
        def greet():
            return "now you are in the greet() function"

        def welcome():
            return "now you are in the welcome() function"

        if name == "yasoob":
            return greet
        else:
            return welcome

    a = hi()
    print a
    #outputs: <function greet at 0x7f2143c01500>

    #This clearly shows that `a` now points to the greet() function in hi()
    #Now try this

    print a()
    #outputs: now you are in the greet() function

Just take a look at the code again. In the ``if/else`` clause we are
returning ``greet`` and ``welcome``, not ``greet()`` and ``welcome()``.
Why is that? It is so because when you put parentheses around it the
function gets executed whereas if you don't put parenthesis around it
then it can be passed around and can be assigned to other variables
without executing it. Did you get it ? Let me explain it a little bit in
more detail. When we write ``a = hi()``, ``hi()`` gets executed and
because the name is yasoob by default, the function greet is returned.
If we change the statement to ``a = hi(name = "ali")`` then the welcome
function will be returned. We can also do print ``hi()()`` which outputs
*now you are in the greet() function*.

Giving a function as an argument to another function:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    def hi():
        return "hi yasoob!"

    def doSomethingBeforeHi(func):
        print "I am doing some  boring work before executing hi()"
        print func()

    doSomethingBeforeHi(hi)
    #outputs:I am doing some  boring work before executing hi()
    #        hi yasoob!

Now you have all the required knowledge to learn what decorators really
are. Decorators let you execute code before and after a function.

Writing your first decorator:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the last example we actually made a decorator! Lets modify the
previous decorator and make a little bit more usable program:

::

    def a_new_decorator(a_func):

        def wrapTheFunction():
            print "I am doing some  boring work before executing a_func()"

            a_func()

            print "I am doing some boring work after executing a_func()"

        return wrapTheFunction

    def a_function_requiring_decoration():
        print "I am the function which needs some decoration to remove my foul smell"

    a_function_requiring_decoration()
    #outputs: "I am the function which needs some decoration to remove my foul smell"

    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    #now a_function_requiring_decoration is wrapped by wrapTheFunction()

    a_function_requiring_decoration()
    #outputs:I am doing some  boring work before executing a_function_requiring_decoration()
    #        I am the function which needs some decoration to remove my foul smell
    #        I am doing some boring work after executing a_function_requiring_decoration()

Did you get it? We just applied the previously learned principles. This
is exactly what the decorators do in python! They wrap a function and
modify its behaviour in one way or the another. Now you might be
wondering that we did not use the @ anywhere in our code? That is just a
short way of making up a decorated function. Here is how we could have
run the previous code sample using @.

::

    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey yo! Decorate me!"""
        print "I am the function which needs some decoration to \
        remove my foul smell"

    a_function_requiring_decoration()
    #outputs: I am doing some  boring work before executing a_function_requiring_decoration()
    #         I am the function which needs some decoration to remove my foul smell
    #         I am doing some boring work after executing a_function_requiring_decoration()

    #the @a_new_decorator is just a short way of saying:
    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

I hope you now have a basic understanding of how decorators work in
Python. Now there is one problem with our code. If we run:

::

    print(a_function_requiring_decoration.__name__)
    # Output: wrapTheFunction

That's not what we expected! It's name is
"a\_function\_requiring\_decoration". Well our function was replaced by
wrapTheFunction. It overrided the name and docstring of our function.
Luckily Python provides us a simple function to solve this problem and
that is ``functools.wraps``. Let's modify our previous example to use
``functools.wraps``:

::

    from functools import wraps

    def a_new_decorator(a_func):
        @wraps(a_func)
        def wrapTheFunction():
            print "I am doing some  boring work before executing a_func()"
            a_func()
            print "I am doing some boring work after executing a_func()"
        return wrapTheFunction

    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey yo! Decorate me!"""
        print "I am the function which needs some decoration to \
        remove my foul smell"

    print(a_function_requiring_decoration.__name__)
    # Output: a_function_requiring_decoration

Now that is much better. Let's move on and learn some use-cases of
decorators.

**Blueprint :**

.. code:: python

    from functools import wraps
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Function will not run"
            return f(*args, **kwargs)
        return decorated

    @decorator_name
    def func():
        print "Function is running"

    can_run = True
    print(func())
    # Output: Function is running

    can_run=False
    print(func())
    # Output: Function will not run

Note: ``@wraps`` takes a function to be decorated and adds the
functionality of copying over the function name, docstring, arguments
list, etc. This allows to access the pre-decorated function's properties
in the decorator.

Use-cases:
~~~~~~~~~~

Now let's take a look at the areas where decorators really shine and
their usage makes something really easy to manage.

1. Authorization
^^^^^^^^^^^^^^^^

Decorators can help to check whether someone is authorized to use an
endpoint in a web application. They are extensively used in Flask web
framework and Django. Here is an example to employ decorator based
authentication:

**Example :**

.. code:: python

    from functools import wraps

    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not check_auth(auth.username, auth.password):
                return authenticate()
            return f(*args, **kwargs)
        return decorated

2. Logging
^^^^^^^^^^

Logging is another area where the decorators shine. Here is an example:

.. code:: python

    from functools import wraps

    def logit(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print func.__name__ + " was called"
            return func(*args, **kwargs)
        return with_logging

    @logit
    def addition_func(x):
       """does some math"""
       return x + x


    result = addition_func(4)
    # Output: addition_func was called

I am sure you are already thinking about some clever uses of decorators.
