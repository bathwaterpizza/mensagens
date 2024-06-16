# Como utilizar

### Importando no Principal

```Python
from .mensagens import *
```

### Importando em outros módulos

```Python
from ..mensagens import *
```

### Retornando um código de status

```Python
def func():
	(...)

	if not verifica_dados():
		return Status.DADO_INVALIDO, None
	else:
		return Status.OK, dados
```

### Exibindo uma mensagem de erro no Principal

```Python
err, retorno = func2()
if err != 0:
	# Cancela operação e exibe mensagem de erro
	print(f"Erro: {get_msg_status(err)}")
```

# Documentação

Esse módulo associa códigos de status à mensagens de erro na aplicação. Deve ser utilizado nos módulos internos, para se referir aos erros com a enum `Status`, e no módulo Principal, para exibir as mensagens de erro ao usuário, com `get_msg_status()`.

Lembrando que os códigos em `int` também são códigos de status válidos, a enum `Status` apenas deixa mais claro qual é o erro, dentro do código fonte.
