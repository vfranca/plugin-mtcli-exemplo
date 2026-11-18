# plugin-mtcli-exemplo

Plugin de exemplo para o **mtcli**, demonstrando a estrutura básica de desenvolvimento, instalação e integração de plugins.

## Requisitos

- Python >= 3.10 e < 3.14.
- mtcli instalado.
- pip.

## Instalação

Clone o repositório:

```bash
git clone git@github.com:vfranca/plugin-mtcli-exemplo.git
```

Entre no diretório do projeto:

```bash
cd plugin-mtcli-exemplo
```

Instale o plugin:

```bash
pip install .
```

## Desenvolvimento

Para instalar o projeto em modo editável:

```bash
pip install -e .
```

Essa modalidade permite modificar o código-fonte sem precisar reinstalar o pacote a cada alteração.

## Utilização

Após a instalação, o comando disponibilizado pelo plugin pode ser executado pelo mtcli:

```bash
mt exemplo
```

## Licença

Consulte o arquivo LICENSE para obter informações sobre os termos de utilização e distribuição.
