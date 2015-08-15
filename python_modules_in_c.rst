Python Modules in C
-------------------

We all know that Python can be slow at times. If you are using it to do
some resource intensive task then it can be a major bottleneck. What
options do we have of making it fast apart from code optimisation?
Fortunately Python has a solution for us. It allows us to interface with
C code easily and write extensions for critical parts in C. This allows
to provide a speed boost to our Python code.

There are already a couple of modules which have been rewritten in C for
the sake of speed. They include cPickle, cProfile and c
