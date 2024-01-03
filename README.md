# formscreator

Contexto:
O projeto tem alguns tally que preenchem databases do notion. Alguns desses projetos fazem um esquema de atualização dos dados que já foram submetidos, hoje eu faço através de hidden fields mas isso limita muito a quantidade de campos pre-preenchidos q eu posso utilizar.

Desafio:
Montar um front-end high-code adaptativo para esses casos

Fluxos:
https://miro.com/app/board/uXjVN-Wxcvg=/

## Como executar o projeto:

Este projeto requer o Python 3.8 ou superior. Verifique:

```bash
$ py --version
```

Crie um ambiente virtual Python:

```bash
$ py -m venv NOME_DO_AMBIENTE
```

Ative o ambiente:

```bash
$ source NOME_DO_AMBIENTE/Scripts/activate
```

Instale o requisitos do projeto:

```bash
$ pip install requirements.txt
```

Por fim, execute o projeto:

```bash
$ flask run --deubg
```
###### Nota: "--debug" é opicional