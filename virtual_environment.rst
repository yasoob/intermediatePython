Ambiente Virtual 
-------------------

VOcê já ouviu falar de ``virtualenv``? Se você é um iniciante, 
então deve não ter escutado sobre, mas se você for 
um programador experiente, então deve ser uma parte vital do seu conjunto de ferramentas. 

Então o que é ``virtualenv``? ``Virtualenv`  é uma ferramenta a qual nos permite
criar ambientes isolados de python. Imagine que você tem uma aplicação que
precisa da versão 2 de uma biblioteca, mas outra precisa da versão 3. 
Como você pode usar e desenvolver ambas dessas aplicações?

Se você instalar tudo em ``/usr/lib/python2.7/site-packages`` (ou qual for o local padrão da sua plataforma). é fácil de terminar em uma situação onde você intencionalmente atualiza o pacote.

Em outro caso, imagine que você tem uma aplicação a qual está totalmente 
finalizada e você não quer fazer nenhuma outra mudança para as bibliotecas
que está usando, mas ao mesmo tempo você começou a desenvolver uma outra aplicação 
que requer uma versão atualizada dessas bibliotecas.

O que você irá fazer? Use ``virtualenv``! Um ambiente isolado será criado
para a sua aplicação python e permitirá você instalar bibliotecas Python 
nesse ambiente isolado ao invés de criá-los globalmente.

Para instalar, apenas digite o comando no terminal:

..code:: python
	
	$ pip install virtualenv

Os comandos mais importantes são:

-  ``$ virtualenv myproject``
-  ``$ source bin/activate``

O primeiro irá criar um ambiente isolado na pasta 
``myproject`` e o segundo comando ativa o ambiente isolado.

Enquanto estiver criando a virtualenv você tem que tomar uma decisão. Você
quer que essa virtualenv utilize pacotes do seu sistema ``site-packages``
ou instá-los no site-packages do virtualenv? Por padrão, o
virtualenv não irá dar acesso ao ``site-packages`` global.

.. code:: python

    $ virtualenv --system-site-packages mycoolproject

Você pode desligar a ``env`` digitando:

.. code:: python

    $ deactivate

Rodando `python` e depois desativando o ambiente, o sistema irá utilizar novamente as suas configurações padrões do Python.


**Bonus**

Você pode usar ``smartcd`` que é uma biblioteca para bash e zsh, que lhe 
permite alterar o seu ambiente bash (ou zsh) enquanto troca de pastas (cd). Pode ser útil ativar e desativar a ``virtualenv``quando você muda
os diretórios. Eu tenho usado bastante e amado. Você pode ler mais sobre em GitHub <https://github.com/cxreg/smartcd>`__

Essa foi uma rápida intodução sobre virtualven. Há muito mais sobre; `esse link <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`__ tem mais informações.