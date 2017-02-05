Collections
-----------

Python ships with a module that contains a number of container data
types called Collections. We will talk about a few of them and discuss
their usefulness.

The ones which we will talk about are:

-  ``defaultdict``
-  ``OrderedDict``
-  ``counter``
-  ``deque``
-  ``namedtuple``
-  ``enum.Enum`` (outside of the module; Python 3.4+)

``defaultdict``
^^^^^^^^^^^^^^^^^^^

I personally use defaultdict quite a bit. Unlike ``dict``, with
``defaultdict`` you do not need to check whether a key is present or
not. So we can do:

.. code:: python

    from collections import defaultdict

    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

    favourite_colours = defaultdict(list)

    for name, colour in colours:
        favourite_colours[name].append(colour)

    print(favourite_colours)

    # output
    # defaultdict(<type 'list'>,
    #    {'Arham': ['Green'],
    #     'Yasoob': ['Yellow', 'Red'],
    #     'Ahmed': ['Silver'],
    #     'Ali': ['Blue', 'Black']
    # })

One other very important use case is when you are appending to nested
lists inside a dictionary. If a ``key`` is not already present in the
dictionary then you are greeted with a ``KeyError``. ``defaultdict``
allows us to circumvent this issue in a clever way. First let me share
an example using ``dict`` which raises ``KeyError`` and then I will
share a solution using ``defaultdict``.

**Problem:**

.. code:: python

    some_dict = {}
    some_dict['colours']['favourite'] = "yellow"
    # Raises KeyError: 'colours'

**Solution:**

.. code:: python

    import collections
    tree = lambda: collections.defaultdict(tree)
    some_dict = tree()
    some_dict['colours']['favourite'] = "yellow"
    # Works fine

You can print ``some_dict`` using ``json.dumps``. Here is some
sample code:

.. code:: python

    import json
    print(json.dumps(some_dict))
    # Output: {"colours": {"favourite": "yellow"}}

``OrderedDict``
^^^^^^^^^^^^^^^^^^^

``OrderedDict`` keeps its entries sorted as they are initially inserted.
Overwriting a value of an existing key doesn't change the position of
that key. However, deleting and reinserting an entry moves the key to
the end of the dictionary. 

**Problem:**

.. code:: python

    colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
    for key, value in colours.items():
        print(key, value)
    # Output:
    #   Green 170
    #   Blue 160
    #   Red 198
    # Entries are retrieved in an unpredictable order
   
**Solution:**

.. code:: python

    from collections import OrderedDict
    
    colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
    for key, value in colours.items():
        print(key, value)
    # Output:
    #   Red 198
    #   Green 170
    #   Blue 160
    # Insertion order is preserved

``counter``
^^^^^^^^^^^^^^^

Counter allows us to count the occurrences of a particular item. For
instance it can be used to count the number of individual favourite
colours:

.. code:: python

    from collections import Counter

    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

    favs = Counter(name for name, colour in colours)
    print(favs)
    # Output: Counter({
    #    'Yasoob': 2,
    #    'Ali': 2,
    #    'Arham': 1,
    #    'Ahmed': 1
    # })

We can also count the most common lines in a file using it. For example:

.. code:: python

    with open('filename', 'rb') as f:
        line_count = Counter(f)
    print(line_count)

``deque``
^^^^^^^^^^^^^

``deque`` provides you with a double ended queue which means that you
can append and delete elements from either side of the queue. First of
all you have to import the deque module from the collections library:

.. code:: python

    from collections import deque

Now we can instantiate a deque object.

.. code:: python

    d = deque()

It works like python lists and provides you with somewhat similar
methods as well. For example you can do:

.. code:: python

    d = deque()
    d.append('1')
    d.append('2')
    d.append('3')

    print(len(d))
    # Output: 3

    print(d[0])
    # Output: '1'

    print(d[-1])
    # Output: '3'

You can pop values from both sides of the deque:

.. code:: python

    d = deque(range(5))
    print(len(d))
    # Output: 5

    d.popleft()
    # Output: 0

    d.pop()
    # Output: 4

    print(d)
    # Output: deque([1, 2, 3])

We can also limit the amount of items a deque can hold. By doing this
when we achieve the maximum limit of our deque it will simply pop out
the items from the opposite end. It is better to explain it using an
example so here you go:

.. code:: python

    d = deque(maxlen=30)

Now whenever you insert values after 30, the leftmost value will be
popped from the list. You can also expand the list in any direction with
new values:

.. code:: python

    d = deque([1,2,3,4,5])
    d.extendleft([0])
    d.extend([6,7,8])
    print(d)
    # Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

``namedtuple``
^^^^^^^^^^^^^^^^^^

You might already be acquainted with tuples. A tuple is basically
a immutable list which allows you to store a sequence of values
separated by commas. They are just like lists but have a few key
differences. The major one is that unlike lists, **you can not
reassign an item in a tuple**. In order to access the value in a
tuple you use integer indexes like:

.. code:: python

    man = ('Ali', 30)
    print(man[0])
    # Output: Ali

Well, so now what are ``namedtuples``? They turn tuples into convenient
containers for simple tasks. With namedtuples you don't have to use
integer indexes for accessing members of a tuple. You can think of
namedtuples like dictionaries but unlike dictionaries they are
immutable.

.. code:: python

    from collections import namedtuple

    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")

    print(perry)
    # Output: Animal(name='perry', age=31, type='cat')

    print(perry.name)
    # Output: 'perry'

You can now see that we can access members of a tuple just by their
name using a ``.``. Let's dissect it a little more. A named tuple has two
required arguments. They are the tuple name and the tuple field\_names.
In the above example our tuple name was 'Animal' and the tuple
field\_names were 'name', 'age' and 'type'. Namedtuple makes your tuples
**self-document**. You can easily understand what is going on by having
a quick glance at your code. And as you are not bound to use integer
indexes to access members of a tuple, it makes it more easy to maintain
your code. Moreover, as **`namedtuple` instances do not have
per-instance dictionaries**, they are lightweight and require no more
memory than regular tuples. This makes them faster than dictionaries.
However, do remember that as with tuples, **attributes in namedtuples
are immutable**. It means that this would not work:

.. code:: python

    from collections import namedtuple

    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")
    perry.age = 42

    # Output: Traceback (most recent call last):
    #            File "", line 1, in
    #         AttributeError: can't set attribute

You should use named tuples to make your code self-documenting. **They
are backwards compatible with normal tuples**. It means that you can use
integer indexes with namedtuples as well:

.. code:: python

    from collections import namedtuple

    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")
    print(perry[0])
    # Output: perry

Last but not the least, you can convert a namedtuple to a dictionary.
Like this:

.. code:: python

    from collections import namedtuple

    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="Perry", age=31, type="cat")
    print(perry._asdict())
    # Output: OrderedDict([('name', 'Perry'), ('age', 31), ...

``enum.Enum`` (Python 3.4+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another useful collection is the enum object. It is available in the ``enum``
module, in Python 3.4 and up (also available as a backport in PyPI named ``enum34``.)
Enums (`enumerated type <https://en.wikipedia.org/wiki/Enumerated_type>`_) are
basically a way to organize various things.

Let’s consider the Animal namedtuple from the last example.  It had a ``type``
field.  The problem is, the type was a string.  This poses some problems for
us. What if the user types in ``Cat`` because they held the Shift key?  Or
``CAT``?  Or ``kitten``?

Enumerations can help us avoid this problem, by not using strings.  Consider
this example:

.. code:: python

    from collections import namedtuple
    from enum import Enum

    class Species(Enum):
        cat = 1
        dog = 2
        horse = 3
        aardvark = 4
        butterfly = 5
        owl = 6
        platypus = 7
        dragon = 8
        unicorn = 9
        # The list goes on and on...

        # But we don't really care about age, so we can use an alias.
        kitten = 1
        puppy = 2

    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="Perry", age=31, type=Species.cat)
    drogon = Animal(name="Drogon", age=4, type=Species.dragon)
    tom = Animal(name="Tom", age=75, type=Species.cat)
    charlie = Animal(name="Charlie", age=2, type=Species.kitten)

    # And now, some tests.
    >>> charlie.type == tom.type
    True
    >>> charlie.type
    <Species.cat: 1>


This is much less error-prone.  We have to be specific, and we should use only
the enumeration to name types.

There are three ways to access enumeration members.  For example, all three
methods will get you the value for ``cat``:

.. code:: python

    Species(1)
    Species['cat']
    Species.cat

This was just a quick drive through the ``collections`` module. Make
sure you read the official documentation after reading this.
