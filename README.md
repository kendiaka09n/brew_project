# brew_project

Visite minha documentacao

1. Clone o repositório:

```bash
git clone https://github.com/kendiaka09n/brew_project.git
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.11.9
pyenv local 3.11.9
```

3. Configurar poetry para Python version 3.11.9 e ative o ambiente virtual:

```bash
poetry env use 3.11.9
poetry shell
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
poetry run task test
```

6. Próximos passos:

