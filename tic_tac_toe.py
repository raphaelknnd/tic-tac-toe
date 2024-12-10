# Código criado para praticar o uso de strings e lógica em linguagem Python.
# O jogo da velha (tic-tac-toe) será feito utilziando strings e cada casa será representada por um número tal qual o teclado numérico do pc:
'''  7 | 8 | 9 
    ---+---+---
     4 | 5 | 6 
    ---+---+---
     1 | 2 | 3 '''

vez = 'x'

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


print_result()
#print(divisor())