Object introspection
--------------------
Na programação de computadores, introspeção é a habilidade de determinar
o tipo de um objeto em um tempo de execução. Esse é um dos pontos fortes de Python.
Tudo em Python é um objeto e nós podemos examinar esses objetos.
Python  

Python ships with a few built-in functions and modules to help us.

``dir``
^^^^^^^^^^^

Nessa seção iremos aprender sobre o  ``dir`` e como nos facilita na introspecção. 
É uma das funções mais importantes para introspecção. Uma lista é retornada
com os atributos e métodos que pertencem à um objeto. Aqui vai um exemplo:

.. code:: python

    my_list = [1, 2, 3]
    dir(my_list)
    # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
    # '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
    # '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
    # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
    # '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
    # '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
    # 'remove', 'reverse', 'sort']

Nossa introspecção nos dar os nomes de todos os métodos de uma lista. Isso
pode ser conveniente quando você não consegue lembrar o nome de um método. Se rodarmos
``dir()`` sem nenhum argumento, ele retorna todos os nomes no escopo atual. 

``type`` e ``id``
^^^^^^^^^^^^^^^^^^^^^^^

A função ``type`` retorna o tipo de um objeto. Por exemplo:

.. code:: python

    print(type(''))
    # Output: <type 'str'>

    print(type([]))
    # Output: <type 'list'>

    print(type({}))
    # Output: <type 'dict'>

    print(type(dict))
    # Output: <type 'type'>

    print(type(3))
    # Output: <type 'int'>

``id`` retorna o id exclusivo de vários objetos. Por exemplo:

.. code:: python

    name = "Yasoob"
    print(id(name))
    # Output: 139972439030304

módulo ``inspect`` 
^^^^^^^^^^^^^^^^^^^^^^
O módulo inspect também fornece várias funções úteis para pegar 
informação sobre objetos vivos. Por exemplo, você pode checar os membros 
de um objeto com o comando:  

.. code:: python

    import inspect
    print(inspect.getmembers(str))
    # Output: [('__add__', <slot wrapper '__add__' of ... ...

Há vários outros métodos que também ajudam na introspecção. 
Você pode explorá-los se desejar.

