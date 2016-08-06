Decorators
----------

Decorators are a significant part of Python. In simple words: they are
functions which modify the functionality of another function. They help
to make our code shorter and more Pythonic. Most of the beginners do not
know where to use them so I am going to share some areas where
decorators can make your code more concise.

First, let's discuss how to write your own decorator.

It is perhaps one of the most difficult concepts to grasp. We will take
it one step at a time so that you can fully understand it.

Everything in Python is an object:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First of all let's understand functions in Python:

.. code:: python

    def hi(name="yasoob"):
        return "hi " + name

    print(hi())
    # output: 'hi yasoob'

    # We can even assign a function to a variable like
    greet = hi
    # We are not using parentheses here because we are not calling the function hi
    # instead we are just putting it into the greet variable. Let's try to run this

    print(greet())
    # output: 'hi yasoob'

    # Let's see what happens if we delete the old hi function!
    del hi
    print(hi())
    #outputs: NameError

    print(greet())
    #outputs: 'hi yasoob'

Defining functions within functions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So those are the basics when it comes to functions. Let's take your
knowledge one step further. In Python we can define functions inside
other functions:

.. code:: python

    def hi(name="yasoob"):
        print("now you are inside the hi() function")

        def greet():
            return "now you are in the greet() function"

        def welcome():
            return "now you are in the welcome() function"

        print(greet())
        print(welcome())
        print("now you are back in the hi() function")

    hi()
    #output:now you are inside the hi() function
    #       now you are in the greet() function
    #       now you are in the welcome() function
    #       now you are back in the hi() function

    # This shows that whenever you call hi(), greet() and welcome()
    # are also called. However the greet() and welcome() functions
    # are not available outside the hi() function e.g:

    greet()
    #outputs: NameError: name 'greet' is not defined

So now we know that we can define functions in other functions. In
other words: we can make nested functions. Now you need to learn one
more thing, that functions can return functions too.

Returning functions from within functions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is not necessary to execute a function within another function, we
can return it as an output as well:

.. code:: python

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
    print(a)
    #outputs: <function greet at 0x7f2143c01500>

    #This clearly shows that `a` now points to the greet() function in hi()
    #Now try this

    print(a())
    #outputs: now you are in the greet() function

Just take a look at the code again. In the ``if/else`` clause we are
returning ``greet`` and ``welcome``, not ``greet()`` and ``welcome()``.
Why is that? It's because when you put a pair of parentheses after it, the
function gets executed; whereas if you don't put parenthesis after it,
then it can be passed around and can be assigned to other variables
without executing it. Did you get it? Let me explain it in a little bit
more detail. When we write ``a = hi()``, ``hi()`` gets executed and
because the name is yasoob by default, the function ``greet`` is returned.
If we change the statement to ``a = hi(name = "ali")`` then the ``welcome``
function will be returned. We can also do print ``hi()()`` which outputs
*now you are in the greet() function*.

Giving a function as an argument to another function:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def hi():
        return "hi yasoob!"

    def doSomethingBeforeHi(func):
        print("I am doing some boring work before executing hi()")
        print(func())

    doSomethingBeforeHi(hi)
    #outputs:I am doing some boring work before executing hi()
    #        hi yasoob!

Now you have all the required knowledge to learn what decorators really
are. Decorators let you execute code before and after a function.

Writing your first decorator:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the last example we actually made a decorator! Let's modify the
previous decorator and make a little bit more usable program:

.. code:: python

    def a_new_decorator(a_func):

        def wrapTheFunction():
            print("I am doing some boring work before executing a_func()")

            a_func()

            print("I am doing some boring work after executing a_func()")

        return wrapTheFunction

    def a_function_requiring_decoration():
        print("I am the function which needs some decoration to remove my foul smell")

    a_function_requiring_decoration()
    #outputs: "I am the function which needs some decoration to remove my foul smell"

    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    #now a_function_requiring_decoration is wrapped by wrapTheFunction()

    a_function_requiring_decoration()
    #outputs:I am doing some boring work before executing a_func()
    #        I am the function which needs some decoration to remove my foul smell
    #        I am doing some boring work after executing a_func()

Did you get it? We just applied the previously learned principles. This
is exactly what the decorators do in Python! They wrap a function and
modify its behaviour in one way or the another. Now you might be
wondering that we did not use the @ anywhere in our code? That is just a
short way of making up a decorated function. Here is how we could have
run the previous code sample using @.

.. code:: python

    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey you! Decorate me!"""
        print("I am the function which needs some decoration to "
              "remove my foul smell")

    a_function_requiring_decoration()
    #outputs: I am doing some boring work before executing a_func()
    #         I am the function which needs some decoration to remove my foul smell
    #         I am doing some boring work after executing a_func()

    #the @a_new_decorator is just a short way of saying:
    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

I hope you now have a basic understanding of how decorators work in
Python. Now there is one problem with our code. If we run:

.. code:: python

    print(a_function_requiring_decoration.__name__)
    # Output: wrapTheFunction

That's not what we expected! Its name is
"a\_function\_requiring\_decoration". Well our function was replaced by
wrapTheFunction. It overrode the name and docstring of our function.
Luckily Python provides us a simple function to solve this problem and
that is ``functools.wraps``. Let's modify our previous example to use
``functools.wraps``:

.. code:: python

    from functools import wraps

    def a_new_decorator(a_func):
        @wraps(a_func)
        def wrapTheFunction():
            print("I am doing some boring work before executing a_func()")
            a_func()
            print("I am doing some boring work after executing a_func()")
        return wrapTheFunction

    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey yo! Decorate me!"""
        print("I am the function which needs some decoration to "
              "remove my foul smell")

    print(a_function_requiring_decoration.__name__)
    # Output: a_function_requiring_decoration

Now that is much better. Let's move on and learn some use-cases of
decorators.

**Blueprint:**

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
        return("Function is running")

    can_run = True
    print(func())
    # Output: Function is running

    can_run = False
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

Authorization
~~~~~~~~~~~~

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
                authenticate()
            return f(*args, **kwargs)
        return decorated

Logging
~~~~~~~~~~~~

Logging is another area where the decorators shine. Here is an example:

.. code:: python

    from functools import wraps

    def logit(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + " was called")
            return func(*args, **kwargs)
        return with_logging

    @logit
    def addition_func(x):
       """Do some math."""
       return x + x


    result = addition_func(4)
    # Output: addition_func was called

I am sure you are already thinking about some clever uses of decorators.

Decorators with Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^

Come to think of it, isn't ``@wraps`` also a decorator?  But, it takes an
argument like any normal function can do.  So, why can't we do that too?

This is because when you use the ``@my_decorator`` syntax, you are
applying a wrapper function with a single function as a parameter
Remember, everything in Python is an object, and this includes
functions!  With that in mind, we can write a function that returns
a wrapper function.

Nesting a Decorator Within a Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's go back to our logging example, and create a wrapper which lets
us specify a logfile to output to.

.. code:: python

    from functools import wraps
    
    def logit(logfile='out.log'):
        def logging_decorator(func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + " was called"
                print(log_string)
                # Open the logfile and append
                with open(logfile, 'a') as opened_file:
                    # Now we log to the specified logfile
                    opened_file.write(log_string + '\n')
            return wrapped_function
        return logging_decorator

    @logit()
    def myfunc1():
        pass
        
    myfunc1()
    # Output: myfunc1 was called
    # A file called out.log now exists, with the above string
    
    @logit(logfile='func2.log')
    def myfunc2():
        pass
    
    myfunc2()
    # Output: myfunc2 was called
    # A file called func2.log now exists, with the above string

Decorator Classes
~~~~~~~~~~~~~~~~~

Now we have our logit decorator in production, but when some parts
of our application are considered critical, failure might be
something that needs more immediate attention.  Let's say sometimes
you want to just log to a file.  Other times you want an email sent,
so the problem is brought to your attention, and still keep a log
for your own records.  This is a case for using inheritence, but
so far we've only seen functions being used to build decorators.

Luckily, classes can also be used to build decorators.  So, let's
rebuild logit as a class instead of a function.

.. code:: python

    class logit(object):
        def __init__(self, logfile='out.log'):
            self.logfile = logfile
        
        def __call__(self, func):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(self.logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            # Now, send a notification
            self.notify()
        
        def notify(self):
            # logit only logs, no more
            pass
    
This implementation has an additional advantage of being much cleaner than
the nested function approach, and wrapping a function still will use
the same syntax as before:

.. code:: python

    @logit()
    def myfunc1():
        pass

Now, let's subclass logit to add email functionality (though this topic
will not be covered here).

.. code:: python

    class email_logit(logit):
        '''
        A logit implementation for sending emails to admins
        when the function is called.
        '''
        def __init__(self, email='admin@myproject.com', *args, **kwargs):
            self.email = email
            super(email_logit, self).__init__(*args, **kwargs)
            
        def notify(self):
            # Send an email to self.email
            # Will not be implemented here
            pass

From here, ``@email_logit`` works just like ``@logit`` but sends an email
to the admin in addition to logging.
