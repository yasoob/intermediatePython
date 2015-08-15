Debugging
---------

Debuggin is also something which once mastered can greatly enhance your
bug hunting skills. Most of the newcommers neglect the importance of the
Python debugger (``pdb``). In this section I am going to tell you only a
few important commands. You can learn more about it from the official
documentation.

**Running from commandline**

You can run a script from the commandline using the Python debugger.
Here is an example:

.. code:: python

    $ python -m pdb my_script.py

It would cause the debugger to stop the execution on the first statement
it finds. This is helpful if you script is short. You can then inspect
the variables and continue execution line-by-line.

**Running from inside a script**

You can set break points in the script itself so that you can inspect
the variables and stuff at particular points. This is possible using the
``pdb.set_trace()`` method. Here is an example:

.. code:: python

    import pdb

    def make_bread():
        pdb.set_trace()
        return "I don't have time"

    print(make_bread())

Try running the above script after saving it. You would enter the
debugger as soon as you run it. Now it's time to learn some of the
commands of the debugger.

**Commands:**

-  ``c``: continue execution
-  ``w``: shows the context of the current line it is executing.
-  ``a``: print the argument list of the current function
-  ``s``: Execute the current line and stop at the first possible
   occasion.
-  ``n``: Continue execution until the next line in the current function
   is reached or it returns.

The difference between ``n``\ ext and ``s``\ tep is that step stops
inside a called function, while next executes called functions at
(nearly) full speed, only stopping at the next line in the current
function.

These are just a few commands. ``pdb`` also supports post mortem. It is
also a really handy function. I would highly suggest you to look at the
official documentation and learn more about it.
