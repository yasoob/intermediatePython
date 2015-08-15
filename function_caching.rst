Function caching
----------------

Function caching allows us to cache the return values of a function
depending on the arguments. It can save time when an I/O bound function
is periodically called with the same arguments. Before Python 3.2 we had
to write a custom implementation. In Python 3.2+ there is an
``lru_cache`` decorator which allows us to quickly cache and uncache the
return values of a function.

Let's see how we can use it in Python 3.2+ and the versions before it.

Python 3.2+
^^^^^^^^^^^

Let's implement a ficonnaci calculator and use ``lru_cache``.

.. code:: python

    from functools import lru_cache

    @lru_cache(maxsize=32)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    >>> print([fib(n) for n in range(10)])
    # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

The ``maxsize`` argument tells ``lru_cache`` about how many recent
return values to cache.

We can easily uncache the return values as well by using:

.. code:: python

    fib.cache_clear()

Python 2+
^^^^^^^^^

There are a couple of ways to achieve the same effect. You can create
any type of caching machanism. It entirely depends upon your needs. Here
is a generic cache:

.. code:: python

    from functools import wraps

    def memoize(function):
        memo = {}
        @wraps(function)
        def wrapper(*args):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args)
                memo[args] = rv
                return rv
        return wrapper

    @memoize
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(25)

`Here <https://www.caktusgroup.com/blog/2015/06/08/testing-client-side-applications-django-post-mortem/>`__
is a fine article by Caktus Group in which they caught a bug in Django
which occured due to lru\_cache. It's an interesting read. Do check it
out.
