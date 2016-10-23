Enumerate
---------

Enumerate é uma função interna (*built-in*) do Python. Seu uso não pode ser resumido em uma única linha. Ainda assim, muitos programadores iniciantes e avançados, não tem conhecimento dela. Ela nos permite iterar sobre algo e automaticamente ter um contador nesse processo. Aqui tem um exemplo:

.. code:: python

    for contador, valor in enumerate(alguma_lista):
        print(contador, valor)

Isso não é tudo. A função ``enumerate`` também aceita alguns argumentos opcionais que a torna ainda mais útil.

.. code:: python

    minha_lista = ['maçã', 'banana', 'uva', 'pera']
    for c, valor in enumerate(minha_lista, 1):
        print(c, valor)

    # Saida:
    # 1 maçã
    # 2 banana
    # 3 uva
    # 4 pera

Esse argumento opcional permite-nos dizer para a função ``enumerate`` a partir de onde começar o indice. Você também pode criar tuplas contendo o indice e o item da lista usando um ``list``. Aqui tem um exemplo:

.. code:: python

    minha_lista = ['maçã', 'banana', 'uva', 'pera']
    lista_contador = list(enumerate(minha_lista, 1))
    print(lista_contador)
    # Saida: [(1, 'maçã'), (2, 'banana'), (3, 'uva'), (4, 'pera')]

