# 🚀 Python Power Up 🚀

Este projeto foi desenvolvido para automação de tarefas, feito em Python, e ele realiza um cadastro de produtos em um sistema de empresa. Foi construído para facilitar o trabalho de funcionários que precisam abrir uma planilha de Excel e cadastrar manualmente cada produto no sistema da empresa.

## 📚 Funcionalidades

- **Abrir o sistema**: O script procura o Google Chrome no menu Iniciar do Windows, executa e digita o endereço da URL do sistema da empresa.
- **Acessar o login**: Realiza login com o e-mail e senha fornecidos no código.
- **Leitura da base de dados**: Usando a biblioteca Pandas, o sistema lê os dados dos produtos cadastrados e os armazena para automação.
- **Cadastrar produtos**: Automatiza o cadastro dos produtos, incluindo ID, categoria, preço unitário, entre outros detalhes.
- **Interrupção da automação**: Segurando a tecla `ESC`, a execução do código é interrompida.

## 🖥️ Tecnologias usadas

- **Python**: Linguagem de programação utilizada.
- **PyAutoGUI**: Biblioteca para automação de ações com teclado, mouse e tela.
- **Pandas**: Biblioteca para análise e tratamento de dados.
- **Time**: Biblioteca para manipulação de datas e horários.
- **Keyboard**: Biblioteca para capturar eventos de teclado em sistemas operacionais.

## 🔨 Requisitos

Para rodar o código, você precisará instalar alguns programas:

- [VSCode](https://code.visualstudio.com/): Editor de código.
- [Python](https://www.python.org/): Linguagem de programação.

## 🕹️ Como executar

Para executar o projeto, siga os passos abaixo:

1. Baixe o repositório do projeto.
2. Abra o projeto no **VSCode**.
3. Instale as bibliotecas necessárias: **PyAutoGUI**, **Pandas** e **Keyboard**.

### 💡 Instalação das Bibliotecas

Abra o terminal no VSCode e execute o seguinte comando:

```bash
pip install pyautogui pandas keyboard
