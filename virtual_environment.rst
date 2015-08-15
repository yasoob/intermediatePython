Virtual Environment
-------------------

Have you ever heard of ``virtualenv``? The chances are that if you are a
beginner then you might not have heard about it but if you are a
seasoned programmer than it's a vital part of your toolset. So what
``virtualenv`` really is? ``Virtualenv`` is a tool which allows us to
make isolated python environments. Imagine you have an application that
needs version 2 of a LibraryBar, but another application requires
version 3. How can you use and develop both these applications?

If you install everything into ``/usr/lib/python2.7/site-packages`` (or
whatever your platform's standard location is), it's easy to end up in a
situation where you unintentionally upgrade a package that shouldn't be
upgraded. In another case just imagine that you have an application
which is fully developed and you do not want to make any change to the
libraries it is using but at the same time you start developing another
application which requires the updated versions of those libraries. What
will you do? It is where ``virtualenv`` comes into play. It creates
isolated environments for you python application and allows you to
install Python libraries in that isolated environment instead of
installing them globally.

In order to install it just type this command in the shell:

.. code:: python

    $ pip install virtualenv

Now i am going to list some of it's commands. The most important ones
are:

-  ``$ virtualenv myproject``
-  ``$ source bin/activate``

This first one makes an isolated virtualenv environment in the
``myproject`` folder and the second command activates that isolated
environment. While running the first command you have to make a
decision.

Do you want this virtualenv to use packages from your system
``site-packages`` or install them in the virtualenv’s site-packages? By
default, virtualenv will symlink to your system’s ``site-packages`` if
you install a package in the virtualenv that is already installed on
your system. If you want a totally isolated ``virtualenv`` then you’ll
want to do the latter. To do this, you pass in the
``-–no-site-packages`` switch when creating your virtualenv like this:

.. code:: python

    $ virtualenv --no-site-packages mycoolproject

Now you can install any library without disturbing the global libraries
or the libraries of the other environments. You can turn off the ``env``
by typing:

.. code:: python

    $ deactivate

**Bonus**

You can use ``smartcd`` which is a library for bash and zsh and allows
you to alter your bash (or zsh) environment as you cd. It can be really
helpful to activate and deactivate a ``virtualenv`` when you change
directories. I have used it quite a lot and love it. You can read more
about it on `GitHub <https://github.com/cxreg/smartcd>`__

This was just a short intro to virtualenv. There's a lot more to it. For
further study i recommend `this
link. <http://docs.python-guide.org/en/latest/dev/virtualenvs.html>`__
It will remove all of your confusions about virtualenv.
