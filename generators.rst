Geradores
----------

Primeiramente vamos entender o que são iteradores. De acordo com o Wikipedia, um iterador
é um objeto que possibilita ao desenvolvedor percorrer um conjunto de dados, particurlamente listas.
O iterador dá acesso aos elementos dentro do conjunto de dados, mas ele não faz a iteração.
Você deve estar confuso, então vamos mais devagar. Existem três partes chamadas:

- Iterável
- Iterador
- Iteração

Todas essas partes estão conectadas uma com as outras. Iremos discutir cada uma.

Iterável
^^^^^^^^

Um objeto ``iterável`` é qualquer objeto em Python que possui um método ``__iter__`` ou um método
``__getitem__`` definido que retorna um **iterador** ou que pode ter índices (Ambos os métodos já
foram explicados em capítulos anteriores). Em resumo, um objeto ``iterável`` é qualquer objeto 
que nos fornece um **iterador**. E, o que é um **iterador**?

Iterador
^^^^^^^^

Um iterador é qualquer objeto em Python que possui um método ``next`` (Python2)
ou um método ``__next__`` definido. Agora vamos entender o que é **iteração**.

Iteração
^^^^^^^^^

Em poucas palavras, iteração é o processo de pegar um item de algum coisa, por exemplo uma lista.
Quando nós utilizamos um laço para iterar alguma coisa é chamado de iteração. É o nome dado ao 
próprio processo. Agora que nós já sabemos o básico desses termos vamos entender **geradores**.

Geradores
^^^^^^^^^^

Geradores são iteradores, mas você só consegue iterar com eles uma vez.
Isso acontece porque eles não armazenam todos os valores na memória, eles geram 
os valores em tempo real. Você os utiliza iterando sobre eles, sendo com um laço 'for' 
ou passando eles para alguma função ou construtor que itera. A maior parte do tempo 
``geradores`` são implemenatados como funções. No entanto, eles não ``retornam`` um valor, eles
``produzem`` um. Abaixo você encontrará um exemplo simples de uma função ``geradora``.

.. code:: python

    def generator_function():
        for i in range(10):
            yield i

    for item in generator_function():
        print(item)

    # Output: 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

Nesse exemplo a função não é muito útil. Geradores são melhores utilizados 
para calcular grandes conjuntos de resultados (particurlamente cálculos envolvendo
laços) onde você não deseja alocar a memória para todos os resultados ao mesmo tempo.
Muitas funções de Bibliotecas Padrão que retornam ``listas`` no Pytho 2 estão sendo modificadas 
para retornar ``geradores`` no Python 3 porque ``geradores`` precisam de menos recursos.
Aqui segue um exemplo de ``gerador`` que calcula a sequência de Fibonacci:

.. code:: python

    # generator version
    def fibon(n):
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b

E nós podemos utilizar a função da seguinte forma:

.. code:: python

    for x in fibon(1000000):
        print(x)

Dessa forma nós não precisamos nos preocupar se a função está utilizando 
muitos recursos. No entanto, se tivéssemos implementado assim:

.. code:: python

    def fibon(n):
        a = b = 1
        result = []
        for i in range(n):
            result.append(a)
            a, b = b, a + b
        return result

A função teria utilizado todos os nossos recursos para calcular uma entrada muito grande.

Discutimos anteriormente que podemos iterar sobre ``geradores`` apenas uma vez, mas não chegamos a testar isso.
Antes de testar, você precisa saber sobre mais uma função embutida do Python, ``next()``. Ela nos permite 
acessar o próximo elemento da sequência. Vamos testar:

.. code:: python

    def generator_function():
        for i in range(3):
            yield i

    gen = generator_function()
    print(next(gen))
    # Output: 0
    print(next(gen))
    # Output: 1
    print(next(gen))
    # Output: 2
    print(next(gen))
    # Output: Traceback (most recent call last):
    #            File "<stdin>", line 1, in <module>
    #         StopIteration

Como você pode ver, depois de produzir todos os valores, ``next()`` provocou 
um erro` `StopIteration``. Basicamente esse erro nos informa que todos os valores já foram 
produzidos. Você deve está se perguntando o motivo pelo qual esse erro não foi causado quando
usamos o laço ``for``? Bom, a resposta é simples. O laço ``for`` automaticamente pega o erro e 
encerra a chamada do método ``next``. Você sabia que alguns tipos de dados embutidos de Python 
também suportam iteração? Vamos dar uma olhada:

.. code:: python

    my_string = "Yasoob"
    next(my_string)
    # Output: Traceback (most recent call last):
    #      File "<stdin>", line 1, in <module>
    #    TypeError: str object is not an iterator

Bom, isso não é o que esperávamos. O erro diz que ``str`` não é um iterador.
E isso está certo! ``str`` é iterável, mas não é um iterador. Isso significa que ``str``
suporta iteração, mas nós não podemos iterar sobre ela diretamente. Então, como podemos 
iterar sobre ela? É hora de aprender sobre mais uma função embutida do Python, ``iter``.
Ela retorna um objeto ``iterador`` a partir de um objeto iterável. Enquanto um ``int``
não é iterável, nós podemos utilizá-lo em uma string que é iterável. 

.. code:: python

    int_var = 1779
    iter(int_var)
    # Output: Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: 'int' object is not iterable
    # This is because int is not iterable
    
    my_string = "Yasoob"
    my_iter = iter(my_string)
    next(my_iter)
    # Output: 'Y'

Agora está muito melhor. Tenho certeza que você amou aprender sobre geradores. 
Tenha em mente que você só entenderá completamento o conceito quando utilizá-lo.
Tenha certeza de seguir esse padrão e utilizar ``geradores`` sempre que fizer sentido
para você. Você não ficará desapontado!.

