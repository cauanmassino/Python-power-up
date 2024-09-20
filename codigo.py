# A primeira coisa que vamos fazer para construir um codigo 
# é escrever em portugues PASSO A PASSO do projeto

# Passo 1 - Abrir o chrome e acessar o site
#     Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Pegar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos     


#bibliotecas - pyautogui (automatizar algumas instrucoes) | time (tempo - delay em uma linha especifica) | pandas (ajuda na analise de dados) openpyxl e numpy

# pyautogui - Pacote de codigo que ajuda AUTOMATIZAR o teclado, mouse e a tela do computador
# pyautogui.press - Automatizar para pressionar alguma tecla do teclado
# pyautogui.write - Serve para escrever com o teclado (como se fosse você digitando)
# pyautogui.click - Automatizar o click do mouse
# pyautogui.hotkey - Serve para combinação de teclas (crl + a)
# pyautogui.scroll - Serve para rolar com o mouse
# pyautogui.PAUSE(tempo) - Serve para ter um delay entre cada comando que for adicionado
# pyautogui.position - Serve para colocar a posicao do ponteiro do mouse na tela em x e y (x é horizontal e y é vertical)

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1.5 # a cada executacao ele vai esperar 1.5 segundos para nao dar problema no codigo

# Primeiro passo para automatizar é abrir o windows e acessar o chrome para entrar no site da empresa
pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # esperar 3 segundos para carregar a pagina

# Segundo passo para automatizar o login é mexer o ponteiro do mouse até a aba de login e acessar
pyautogui.click(x=925, y=372)

# ctrl a para caso o chrome entrar com outro login automaticamente, entao ele ira apagar e entrar automaticamente com o login correto
pyautogui.hotkey("ctrl", "a")
pyautogui.write("automacaopy@hotmail.com")

# mudar para aba de baixo (tab)
pyautogui.press("tab")
pyautogui.write("automacao123")

#clicar para se logar no site
pyautogui.click(x=955, y=534)
time.sleep(3) # esperar 3 segundos para carregar a pagina

# Terceiro passo para pegar a base de dados

tabela = pandas.read_csv("produtos.csv")

# Quarto passo cadastrar um produto

import keyboard

for linha in tabela.index: # loop infinito para cadastrar base de dados 

    pyautogui.scroll(1000)

    time.sleep(1)

    #checará se a tecla ESC foi pressionada
    if keyboard.is_pressed('esc'):
        #caso tenha sido pressionada, interromperá o loop 
        print('Processo interrompido pelo usuário')
        break
    
    pyautogui.PAUSE = 0.5 # Deixar mais rapido o preenchimento da base de dados

    pyautogui.click(x=851, y=257) # clicar no primeiro campo do produto
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # pegar o codigo da base de dados da tabela e escrever

    pyautogui.press("tab") # passar para proximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) # pegar a marca da base de dados da tabela e escrever

    pyautogui.press("tab") # passar para proximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"])) # pegar o tipo da base de dados da tabela e escrever

    pyautogui.press("tab") # passar para proximo campo
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # pegar a categoria da base de dados da tabela e escrever

    pyautogui.press("tab") # passar para proximo campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # pegar o preco_unitario da base de dados da tabela e escrever

    pyautogui.press("tab") # passar para proximo campo
    pyautogui.write(str(tabela.loc[linha, "custo"])) # pegar o custo da base de dados da tabela e escrever
    pyautogui.press("tab") # passar para proximo campo

    obs = (str(tabela.loc[linha, "obs"])) 
    if obs != "nan": # verifica se existe informacao em obs, caso contrario nao preenche
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para proximo campo
    pyautogui.press("enter")
    pyautogui.scroll(-1000)    
    






