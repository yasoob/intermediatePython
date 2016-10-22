Debugging
---------

Debugging é algo que uma vez compreendido pode te ajudar enormemente
em sua capacidade de encontrar erros (bugs). A maioria dos iniciantes 
negligencia a importancia do Python debugger (``pdb``). Nesta seção,
eu vou mostrar alguns comandos importantes. Você pode aprender mais 
sobre isso a partir da documentação oficial.

**Rodando a partir da linha de comando**

Quando você roda um script a partir da linha de comando usando um
Python debugger. Aqui está um exemplo:

.. code:: python

    $ python -m pdb my_script.py

Este comando faz com que o debuuger pare a execução do código na primeira
linha de comando que ele encontrar. Isso é muito útil se o seu script for
pequeno. Você pode inspecionar as variáveis e continuar a execução linha
por linha.

**Rodando de dentro de um script**

Você pode inserir pontos de quebra (break points) dentro do próprio script
para que você inspecione as variáveis e demais itens em pontos específicos do
seu código. Isso é possível utilizando o método ``pdb.set_trace()``.
Aqui está um exemplo:

.. code:: python

    import pdb

    def make_bread():
        pdb.set_trace()
        return "Eu não tenho tempo"

    print(make_bread())

Tente rodar o script acima após salvá-lo. Você irá entrar no debugger
assim que você o rodar. Agora é hora de aprender alguns dos comandos 
do debugger.

**Comandos:**

-  ``c``: continua a execução
-  ``w``: mostra o contexto da linha atual que ele estpa executando
-  ``a``: mostra a lista de argumentos da função atual
-  ``s``: executa a linha atual e para a execução assim que possível
-  ``n``: continua a execução até a próxima linha da função atual ou o seu retorno

A diferença entre ``n``\ ext e ``s``\ tep  é que o método step para a execução
dentro da função que foi chamada, enquanto o método next executa a função
chanada em (quase) velocidade total, apenas parando na próxima linha da função
onde o pdb foi inserido.

Esses são apenas alguns comandos. ``pdb`` também suporta post mortem. Esta é
realmente uma função muito útil. Eu também sugiro que você olhe a documentação
oficial e aprenda mais sobre isso.
