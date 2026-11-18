# plugin-mtcli-exemplo

Plugin de exemplo para o **mtcli**, demonstrando a estrutura de um pacote Python, sua integração com a CLI e as práticas recomendadas para desenvolvimento de plugins.

## Requisitos

- Python >= 3.10 e < 3.14.
- mtcli instalado.
- pip.

## Estrutura do projeto

O projeto utiliza o modelo `src layout`, recomendado para organização de pacotes Python.

```text
plugin-mtcli-exemplo/
├── src/
│   └── plugin_mtcli_exemplo/
│       ├── __init__.py
│       ├── cli.py
│       └── conf.py
├── tests/
├── .gitattributes
├── .gitignore
├── prek.toml
├── pyproject.toml
└── README.md
```

### Diretórios e arquivos

- `src/plugin_mtcli_exemplo/`: código-fonte do plugin.
- `__init__.py`: inicialização do pacote.
- `cli.py`: implementação dos comandos da CLI.
- `conf.py`: configurações e constantes do plugin.
- `tests/`: testes automatizados.
- `.gitattributes`: configurações de tratamento de arquivos pelo Git.
- `.gitignore`: arquivos e diretórios ignorados pelo Git.
- `prek.toml`: configuração dos hooks de qualidade de código.
- `pyproject.toml`: metadados, dependências e configuração do pacote.
- `README.md`: documentação do projeto.

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

## Utilização

Após a instalação, execute o comando disponibilizado pelo plugin:

```bash
mt exemplo
```

## Desenvolvimento

Para desenvolver o plugin, recomenda-se utilizar um ambiente virtual.

Crie o ambiente:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale o projeto em modo editável:

```bash
pip install -e .
```

O modo editável permite modificar o código-fonte sem precisar reinstalar o pacote a cada alteração.

## Qualidade de código

O projeto utiliza Ruff para análise estática e formatação do código Python, além de Prek para execução dos hooks de qualidade.

Execute os hooks:

```bash
prek run --all-files
```

## Testes

Execute os testes automatizados com:

```bash
pytest
```

## Construção e distribuição

Para gerar os pacotes de distribuição:

```bash
python -m build
```

Para verificar os pacotes gerados:

```bash
twine check dist/*
```

## Licença

Consulte o arquivo LICENSE para obter informações sobre os termos de utilização e distribuição.
