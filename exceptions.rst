Exceções
--------

O tratamento de exceção é uma arte que uma vez dominada te concede imensos
poderes. Eu irei mostrar para você algumas das maneiras que podemos tratar
exceções.

Na teminologia básica estamos cientes da cláusula ``try/except``. O código
que pode causar a ocorrência de uma exceção é colocado dentro do bloco ``try``
e o tratamento da exceção é implementado no bloco ``except``. Aqui está um
exemplo simples:

.. code:: python

    try:
        arquivo = open('teste.txt', 'rb')
    except IOError as e:
        print('Ocorreu um IOError. {}'.format(e.args[-1]))

No exemplo acima tratamos apenas a exceção IOError. O que a maioria dos
iniciantes não sabem é que podemos lidar com múltiplas exceções.

Tratando multiplas exceções:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nós podemos utilizar três métodos para tratar múltiplas exceções. O primeiro
envolve colocar todas as exceções que são prováveis de ocorrer em uma tupla.
Por exemplo:

.. code:: python

    try:
        arquivo = open('teste.txt', 'rb')
    except (IOError, EOFError) as e:
        print("Ocorreu um erro. {}".format(e.args[-1]))

Outro método é tratar individualmente cada exceção em separados blocos
``except``. Podemos ter quantos blocos ``except`` quisermos. Aqui está um
exemplo:

.. code:: python

    try:
        arquivo = open('teste.txt', 'rb')
    except EOFError as e:
        print("Ocorreu um erro EOF.")
        raise e
    except IOError as e:
        print("Ocorreu um erro.")
        raise e

Desta maneira se uma exceção não for tratada pelo primeiro bloco ``except``
então ela poderá ser tratada pelo bloco seguinte, ou por nenhum. Agora o
último método envolve pegar TODAS as exceções:

.. code:: python

    try:
        arquivo = open('teste.txt', 'rb')
    except Exception:
        # Algum log se você desejar
        raise

Isto pode ser útil quando você não tem ideia sobre quais exceções serão
lançadas por seu programa.

Cláusula ``finally``
~~~~~~~~~~~~~~~~~~~~

Envolvemos nosso código principal na cláusula ``try``. Depois disso,
envolvemos um código na cláusula ``except`` que é executado se ocorrer uma
exceção no código envolvido na cláusula ``try``. Neste exemplo usaremos uma
terceira cláusula conhecida como ``finally``. O código envolvido na cláusula
``finally`` será executado independente se uma exceção ocorrer ou não. Ela
pode ser utilizada em ações de limpeza depois de um script. Aqui está um
exemplo simples:

.. code:: python

    try:
        arquivo = open('teste.txt', 'rb')
    except IOError as e:
        print('Ocorreu um IOError. {}'.format(e.args[-1]))
    finally:
        print("Isto seria impresso independente se uma exceção ocorrer ou não!")
        
    # Resultado: Ocorreu um IOError. No such file or directory
    # Isto seria impresso independente se uma exceção ocorrer ou não!

Cláusula ``try/else``
~~~~~~~~~~~~~~~~~~~~~

Muitas vezes queremos que um código execute caso **nenhuma** exceção ocorra.
Isto pode ser facilmente alcançado utilizando uma cláusula ``else``. Alguém
pode perguntar: Se você apenas deseja executar um código caso nenhuma exceção
ocorra, por que você simplesmente não coloca este código dentro do ``try``?
A resposta é que desta forma nenhuma exceção neste código será pega através
do ``try``, e você pode não querer isto. Muitas pessoas não utilizam este
método, e honestamente, nem mesmo eu o utilizo com frequência. Segue um
exemplo:

.. code:: python

    try:
        print('Eu tenho certeza que nenhuma exceção ocorrerá!')
    except Exception:
        print('exceção')
    else:
        # determinado código será executado apenas se nenhuma exceção ocorrer
        # no bloco try, porém, NENHUMA exceção será pega
        print('Isto só seria executado caso nenhuma exceção ocorra. 
              'E um erro aqui não seria pego.')
    finally:
        print('Isto seria impresso em todos os casos.')

    # Resultado: Eu tenho certeza que nenhuma exceção ocorrerá!
    # Isto só seria executado caso nenhuma exceção ocorra.
    # Isto seria impresso em todos os casos.

A cláusula ``else`` só seria executada caso nenhuma exceção ocorra e seria
executada antes da cláusula ``finally``.
