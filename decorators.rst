Decoradores
----------

Decoradores são uma parte importante do Python. Em poucas palavras: 
são funções que modificam a funcionalidade de outra função. Eles ajudam
a tornar nosso código mais curto e mais Pythonico. A maioria dos iniciantes
não sabem como utilizá-los, portanto, eu vou mostrar alguns lugares em que
decoradores podem tornar seu código mais conciso. 

Primeramente, vamos discutir como escrever seu próprio decorador.

Isto é, possivelmente, um dos conceitos mais difíceis de compreender. 
Iremos um passo de cada vez para que você possa compreendê-lo em sua totalidade.


Tudo em Python é um objeto:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Primeiramente, vamos entender o que são funções em Python:

.. code:: python

    def hi(name="yasoob"):
        return "hi " + name

    print(hi())
    # resultado: 'hi yasoob'

    # Nós podemos inclusive atribuir uma função à uma variável
    greet = hi
    # Nós não usamos parênteses aqui porque não estamos chamando a função hi
    # ao contrário, estamos apenas colocando a função dentro da variável greet. Vamos tentar rodar o seguinte:

    print(greet())
    # resultado: 'hi yasoob'

    # Vamos verificar o que acontece quando deletamos a antiga função hi!
    del hi
    print(hi())
    # resultado: NameError

    print(greet())
    # resultado: 'hi yasoob'

Definindo funções dentro de funções:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vimos o básico até agora em se tratando de funções. Vamos pegar nossos
conhecimentos e ir um passo além. Em Python podemos definit funções dentro
de outras funções:

.. code:: python

    def hi(name="yasoob"):
        print("você está dentro da função hi()")

        def greet():
            return "agora você está dentro da função greet()"

        def welcome():
            return "agora você está dentro da função welcome()"

        print(greet())
        print(welcome())
        print("agora você está dentro da função hi() novamente")

    hi()
    #resultado: você está dentro da função hi()
    #           agora você está dentro da função greet()
    #           agora você está dentro da função welcome()
    #           agora você está dentro da função hi() novamente

    # Isso mostra que quando você chama a função hi(), as funções greet() e welcome()
    # também são chamadas. Entretanto, as funções greet() e welcome() 
    # não são disponíveis fora da função hi() e.g:

    greet()
    # resultado: NameError: name 'greet' is not defined

Agora sabemos que podemos definir funções dentro de outras funções.
Em outras palavras: podemos criar funções aninhadas. Agora você precisa
aprender outra coisa, que funções também podem retornar funções.

Retornando funções de dentro de funções:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Não é necessário executar a função dentro da outra função, 
nos podemos apenas devolve-la como resultado também: 

.. code:: python

    def hi(name="yasoob"):
        def greet():
            return "agora você está dentro da função greet()"

        def welcome():
            return "agora você está dentro da função welcome()"

        if name == "yasoob":
            return greet
        else:
            return welcome

    a = hi()
    print(a)
    # resultado: <function greet at 0x7f2143c01500>

    # Isso nos mostra claramente que `a` aponta para a função greet() dentro da função hi()
    # Agora tente isto:

    print(a())
    # resultado: agora você está dentro da função greet()

Pare por um momento para olhar o código novamente. Dentro da cláusula ``if/else`` 
estamos retornando ``greet`` e ``welcome``, e não ``greet()`` e ``welcome()``.
Por que isso? É porque quando colocamos os parênteses, as funções são executadas;
enquanto se não pusermos os parênteses após as funções, elas são passadas adiante
e designadas a outras variáveis sem serem executadas. Conseguiu entender? 
Vamos explicar mais detalhadamente. Quando escrevemos ``a = hi()``, a função ``hi()`` 
é executada e porque o nome é yasoob por padrão, a função ``greet`` é retornada.
Se mudarmos a declaração para ``a = hi(name = "ali")`` então a função ``welcome``
será retornada.  Também podemos dar um print da seguinte forma: ``hi()()`` cujo resultado
é *agora vocês está dentro da função greet()*.

Dando uma função como argumento de outra função:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def hi():
        return "hi yasoob!"

    def doSomethingBeforeHi(func):
        print("Estou fazendo alguma coisa entediante antes de executar a função hi()")
        print(func())

    doSomethingBeforeHi(hi)
    # resultado: Estou fazendo alguma coisa entediante antes de executar a função hi()
    #            hi yasoob!

Agora temos todo o conhecimento necessário para aprender o que decoradores
realmente sçao. Decoradores permitem executar algum código antes e depois de uma função.

Escrevendo seu primeiro decorador:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No último exemplo você, na realidade, fez um decorador!
Vamos modificá-lo e fazer um código um pouco mais útil.

.. code:: python

    def a_new_decorator(a_func):

        def wrapTheFunction():
            print("Estou fazendo algo entediante antes de executar a_func()")

            a_func()

            print("Estou fazendo algo entediante depois de executar a_func()")

        return wrapTheFunction

    def a_function_requiring_decoration():
        print("Estou sou a função que precisa de decorador para remover meu mau cheiro")

    a_function_requiring_decoration()
    # resultado: "Estou sou a função que precisa de decorador para remover meu mau cheiro"

    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    # agora a função a_function_requiring_decoration stá aninhada na função wrapTheFunction()

    a_function_requiring_decoration()
    # resultado: Estou fazendo algo entediante antes de executar a_func()
    #            Estou sou a função que precisa de decorador para remover meu mau cheiro
    #            Estou fazendo algo entediante depois de executar a_func()

Você percebeu? Acabamos de aplicar os conceitos que aprendemos. 
Isso é exatamente o que decoradores fazem em Python! Eles aninham uma função
e modificam o seu comportamento de uma maneira ou de outra. Agora você
deve estar se perguntando o porque não usamos o @ em nenhum lugar do nosso código?
Este é só uma maneira rápida de criar uma função com decorador. Aqui está um
exemplo de como devemos usar o @ no exemplo anterior.

.. code:: python

    @a_new_decorator
    def a_function_requiring_decoration():
        """Ei você! Decore-me!"""
        print("Eu sou a função que precisa de um decorador "
              "para remover meu mau cheiro!")

    a_function_requiring_decoration()
    # resultado: Estou fazendo algo entediante antes de executar a_func()
    #            Estou sou a função que precisa de decorador para remover meu mau cheiro
    #            Estou fazendo algo entediante depois de executar a_func()

    # a declaração @a_new_decorator é só uma forma resumida de se dizer:
    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

Espero que você tenha entendido o básico de como decoradores funcionam
em Python. No entanto, temos um problema com nosso código. Se rodarmos:

.. code:: python

    print(a_function_requiring_decoration.__name__)
    # resultado: wrapTheFunction

Isso não é o que esperávamos! O nome da função é 
"a\_function\_requiring\_decoration". Bem, nossa função na verdade
foi substituída pela função wrapTheFunction. Esta reescreveu o nome
e o docstring da nossa função.
Por sorte, Python nos provê uma função simples para resolver este 
problema cujo nome é ``functools.wraps``. 
Vamos modificar nosso exemplo anterior para usar ``functools.wraps``:

.. code:: python

    from functools import wraps

    def a_new_decorator(a_func):
        @wraps(a_func)
        def wrapTheFunction():
            print("Estou fazendo algo entediante antes de executar a_func()")
            a_func()
            print("Estou fazendo algo entediante depois de executar a_func()")
        return wrapTheFunction

    @a_new_decorator
    def a_function_requiring_decoration():
        """Ei você! Decore-me!"""
        print("Eu sou a função que precisa de um decorador "
              "para remover meu mau cheiro!")

    print(a_function_requiring_decoration.__name__)
    # resultado: a_function_requiring_decoration


Agora sim, está muito melhor. Vamos seguir em frente e aprender alguns
casos de uso de decoradores.

**Blueprint:**

.. code:: python

    from functools import wraps
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Função não irá rodar"
            return f(*args, **kwargs)
        return decorated

    @decorator_name
    def func():
        return("Função está rodando")

    can_run = True
    print(func())
    # resultado: Função está rodando

    can_run = False
    print(func())
    # Output: Função não irá rodar

Nota: ``@wraps`` pega uma função que deve ser decoradas e adiciona
a funcionalidade de copiar o nome da função bem como os docstrings,
argumentos, listas, etc. Isso permite acessar as propriedades da função
pré-decorada no decorador.

Casos de Uso:
~~~~~~~~~~~~~~

Agora vamos dar uma olhada em área onde decoradores realmente brilham
e seu uso realmente facilita a sua manutenção.

Authorização
~~~~~~~~~~~~

Decoradores podem ajudar a checar se alguém está autorizado a usar
um endpoint da sua aplicação web. Eles são extensivamente usados em
nos frameworks Flask e Django. Aqui está um exemplo para empregar um
decorador baseado em autenticação:

**Example :**

.. code:: python

    from functools import wraps

    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not check_auth(auth.username, auth.password):
                authenticate()
            return f(*args, **kwargs)
        return decorated

Logging
~~~~~~~~~~~~

Logging é outra área onde decoradores brilham. Aqui está um exemplo:

.. code:: python

    from functools import wraps

    def logit(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + " foi chamada")
            return func(*args, **kwargs)
        return with_logging

    @logit
    def addition_func(x):
       """Faz alguma matemática."""
       return x + x


    result = addition_func(4)
    # resultado: addition_func foi chamada

Eu tenho certeza que você já deve estar pensando em usos
inteligentes de decoradores.

Decoradores com argumentos
^^^^^^^^^^^^^^^^^^^^^^^^^^

Vamos pensar com calma, ``@wraps`` não é também um decorador?
Mas, ele pega um argumento da mesma forma que uma função o faz normalmente.
Então, não podemos fazer isso também?

Isso é porque quando você usa a sintaxe ``@my_decorator``, você
está aplicando uma função wrapper (de aninhamento) com uma única
função como parâmetro. Lembre-se, tudo em Python é um objeto, e isso 
inclui funções! Com isso em mente, podemos escrveer uma função que retorna
uma função wrapper (de aninhamento). 

Nesting a Decorator Within a Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vamos voltar ao nosso exemplo de logging, e criar um wrapper
que nos permite especificar um arquivo de log (logfile) para
escrever os retornos.

.. code:: python

    from functools import wraps
    
    def logit(logfile='out.log'):
        def logging_decorator(func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + " foi chamada"
                print(log_string)
                # Abre o logfile e adiciona o resultado
                with open(logfile, 'a') as opened_file:
                    # Agora nos abrimos o logfile específico
                    opened_file.write(log_string + '\n')
            return wrapped_function
        return logging_decorator

    @logit()
    def myfunc1():
        pass
        
    myfunc1()
    # resultado: myfunc1 foi chamada
    # Um arquivo chamado out.log passou a existir e contém a string acima
    
    @logit(logfile='func2.log')
    def myfunc2():
        pass
    
    myfunc2()
    # resultado: myfunc2 foi chamada
    # Um arquivo chamado func2.log passou a existir e contém a string acima

Classes de Decoradores
~~~~~~~~~~~~~~~~~~~~~~~

Agora temos nosso decorador logit em produção, mas algumas
partes da nossa aplicação pode ser considerada críticas, falhas
são algo que devem ter atenção imediata. Vamos dizer que em alguns
momentos você só precisar inserir um log a um arquivo. Outros momentos,
você quer que um email seja enviado, de forma que o problema seja levado 
à sua atenção, e ainda precisa manter um log para seus registros. Isso é
um caso para se usar herança, mas até agora só vimos funções endo usadas
para construir decoradores.

Por sorte, classes também podem ser usadas para construir decoradores.
Vamos reconsturir o decorador logit como uma classe ao invés de uma 
função.

.. code:: python

    class logit(object):
        def __init__(self, logfile='out.log'):
            self.logfile = logfile
        
        def __call__(self, func):
            log_string = func.__name__ + " foi chamada"
            print(log_string)
            # Abre o logfile e adiciona o resultado
            with open(self.logfile, 'a') as opened_file:
                # Agora nos abrimos o logfile específico
                opened_file.write(log_string + '\n')
            # Agora mandamos uma notificação
            self.notify()
        
        def notify(self):
            # o decorador logit apenas grava o log no arquivo, nada mais
            pass

Esta implementação tem uma vantagem adicional de ser muito mais clara
que o método de aninhamento de funções, e o decorador será usado em uma
função com a mesma sintaxe anterior:

.. code:: python

    @logit()
    def myfunc1():
        pass

Agora, vamos modificar o decorador logit para adicionar a 
funcionalidade de email (apesar desse tópico não ser coberto aqui). 

.. code:: python

    class email_logit(logit):
        '''
        Uma implementação de logit para envio de emails para os adminstradores
        quando essa função for chamada.
        '''
        def __init__(self, email='admin@myproject.com', *args, **kwargs):
            self.email = email
            super(email_logit, self).__init__(*args, **kwargs)
            
        def notify(self):
            # Manda um email para self.email
            # Isto não será implementado aqui
            pass

A partir daqui, ``@email_logit`` funcionará da mesma forma que ``@logit`` mas
irá enviar um email para o administrador ao mesmo tempo que modificará o arquivo de log.
