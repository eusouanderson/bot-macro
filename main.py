import pyautogui
import string
from random import randint
from time import sleep

x, y = pyautogui.size()
print(x, y)
time = randint(0, 5)

def mouse(email, senha):
    '''pyautogui.hotkey('alt', 'tab')'''
    sleep(2)
    pyautogui.click(1339, 45) # abrir pagina anonima
    sleep(1)
    pyautogui.click(1250, 124) # clicar pg anonima
    sleep(1)
    pyautogui.hotkey('ctrl', 'v') # colar link
    sleep(1)
    pyautogui.hotkey('enter') # apertar enter
    sleep(4)
    pyautogui.click(1185, 98) # clikar no botao c<functiondst
    sleep(2)
    pyautogui.click(721, 232) # selecionar email
    sleep(2)
    pyautogui.click(729, 278) # clikar na aba email
    pyautogui.write(f'{email}', interval=0.15) # escrever email
    pyautogui.click(787, 335) # clikar na aba senha
    sleep(time)
    pyautogui.write(f'{senha}', interval=0.15) # escrever senha
    pyautogui.click(781, 480)
    sleep(5)
    pyautogui.click(772, 325)

    pyautogui.hotkey('alt', 'f4')




def email():
    email = []
    for l in range(0, 6):
        letras = string.ascii_letters[randint(0, 23)]
        email.append(str(letras))

        print(max(email), end=' ')


    return ''.join(email).replace("'", "")+'@outlook.com '

def senha():
    senha = []
    for l in range(0, 5):
        letras = string.ascii_letters[randint(0, 23)]
        senha.append(letras)


    return email



while True:

    mouse(email(), senha())


