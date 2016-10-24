Co-rotinas
----------

Co-rotinas e geradores são similares com umas poucas diferenças. As principais 
diferenças são:

- geradores são produtores de dados
- co-rotinas são consumidoras de dados

Primeiramente, vamos revisar o processo de criação de um gerador. Podemos
criar um gerador da seguinte forma:

.. code:: python

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a+b


Nós utilizamos isso normalmente dentro de um laço ``for``, como no exemplo abaixo:

.. code:: python

    for i in fib():
        print(i)


Isso é rápido e não coloca muito pressão na memória porque ela **gera** os
valores em tempo real em vez de armazená-lo numa lista. Agora, se utilizármos
``yield`` como no exemplo abaixo, de forma geral nós iremos ter uma co-rotina.
Co-rotina consome valore que são enviados para ela. Um exemplo muito básico seria um
``grep`` alternativo em Python:

.. code:: python

    def grep(pattern):
        print("Searching for", pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line)

Espere! O que ``yield``retorna? Bom, nós o transformamos em uma co-rotina.
Ele não contém nenhum valor inicializado, em vez disso, nós fornecemos os valores
para ele externamente. Nós fornecemos os valores utilizando o método ``.send()``.
Segue um exemplo:

.. code:: python

    search = grep('coroutine')
    next(search)
    # Output: Searching for coroutine
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutines instead!")
    # Output: I love coroutines instead!

Os valores são acessados pelo ``yield``. Por que que nós executamos ``next()``?
Isso é necessário para começar as co-rotinas. Assim como ``geradores``, co-rotinas não 
iniciam a função imediatamente. Em vez disso elas executam isso como resposta aos métodos 
``__next__`` e ``.send()``. Portanto, você precisa executar o método ``next()`` e então
a execução avança para a expressão ``yield`` 

Nós podemos fechar a co-rotina chamando o método ``.close()``:

.. code:: python

    search = grep('coroutine')
    # ...
    search.close()


Há muito mais sobre ``co-rotinas``. Eu sugiro você dar uma olhada nessa `maravilhosa
apresentação <http://www.dabeaz.com/coroutines/Coroutines.pdf>`__ por David Beazley.
