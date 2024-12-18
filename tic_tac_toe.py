# Código criado para praticar o uso de strings e lógica em linguagem Python.
# O jogo da velha (tic-tac-toe) será feito utilziando strings e cada casa será representada por um número tal qual o teclado numérico do pc:
'''  7 | 8 | 9 
    ---+---+---
     4 | 5 | 6 
    ---+---+---
     1 | 2 | 3 '''

import os

range = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
game = [" 7 | 8 | 9 ", " 4 | 5 | 6 ", " 1 | 2 | 3 "]

def divisor():
    return "---+---+---"

def print_result():
    x = 0
    while x < 3:
        print(game[x])
        if x == 2:
            break
        print(divisor())
        x += 1

def mark_x(play):
    i = 0
    while i < 3:
        if play in game[i]:
            game[i] = game[i].replace(play, 'x')
            break
        #else:
        #    print('Posição ocupada. Joga de novo.')
        
        i+=1

def mark_o(play):
    i = 0
    while i < 3:
        if play in game[i]:
            game[i] = game[i].replace(play, 'o')
            break
        #else:
        #    print('Posição ocupada. Joga de novo.')
        
        i+=1

def win_condition(vez):
    os.system('cls')
    print_result()

    i = 0
    while i < 3:
        if game[i].count(vez) == 3:
            print(f"{vez} win")
            return False
            
        i+=1

    i = 1
    while i < 10:
        if game[0][i] == vez and game[1][i] == vez and game[2][i] == vez:
            print(f"{vez} win")
            return False
        i+=4

    if (game[0][1] == vez and game[1][5] == vez and game[2][9] == vez) or (game[0][9] == vez and game[1][5] == vez and game[2][1] == vez):
        print(f"{vez} win")
        return False

    return True

def play():

    vez = 'x'
    win = True

    while win:
        os.system('cls')

        print_result()
        play = input(f'({vez}): ')

        if play not in range:
            print('Informe uma posição válida.')
            continue

        if vez == 'x':
            mark_x(play)
            win = win_condition(vez)
            vez = 'o'
        else:
            mark_o(play)
            win = win_condition(vez)
            vez = 'x'
        

play()