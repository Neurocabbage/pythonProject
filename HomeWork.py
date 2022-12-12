"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

# text = 'Напишите программу, удаляющую из текста все слова, содержащие абв'
# new_text = list(filter(lambda i: ('а' or 'б' or 'в') not in i, text.split()))
# print(" ".join(new_text))

'''Создайте программу для игры в ""Крестики-нолики"".'''

# print(" Крестики-нолики ")
#
# Board = [[None, None, None], [None, None, None], [None, None, None]]
#
# def draw_board(Board):
#     for row in Board:
#         print(row)
#
# def take_input(player_token, Board):
#    valid = False
#    while not valid:
#         try:
#           a,b = map(int, input("Куда поставим " + player_token+"? Введите координаты через пробел ").split(sep=" "))
#           try:
#              a = int(a)
#              b = int(b)
#           except:
#              print("Некорректный ввод. ")
#              continue
#           if (a or b) >= 0 and (a or b)  <= 2:
#              if (str(Board[a][b]) not in "XO"):
#                 Board[a][b] = player_token
#                 valid = True
#              else:
#                 print("Эта клетка уже занята!")
#           else:
#             print("Некорректный ввод. Введите числа от 0 до 2.")
#         except:
#             print("Некорректный ввод! ")
#
# def check_win(board):
#        if (board[0][0] == board[1][0] == board[2][0] == "X"
#         or board[0][1] == board[1][1] == board[2][1] == "X"
#         or board[0][2] == board[1][2] == board[2][2] == "X"
#         or board[0][0] == board[0][1] == board[0][2] == "X"
#         or board[1][0] == board[1][1] == board[1][2] == "X"
#         or board[2][0] == board[2][1] == board[2][2] == "X"
#         or board[0][0] == board[1][1] == board[2][2] == "X"
#         or board[0][2] == board[1][1] == board[2][0] == "X"):
#             return "X"
#        if (board[0][0] == board[1][0] == board[2][0] == "0"
#         or board[0][1] == board[1][1] == board[2][1] == "0"
#         or board[0][2] == board[1][2] == board[2][2] == "0"
#         or board[0][0] == board[0][1] == board[0][2] == "0"
#         or board[1][0] == board[1][1] == board[1][2] == "0"
#         or board[2][0] == board[2][1] == board[2][2] == "0"
#         or board[0][0] == board[1][1] == board[2][2] == "0"
#         or board[0][2] == board[1][1] == board[2][0] == "0"):
#             return "0"
#
# def main(Board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(Board)
#         if counter % 2 == 0:
#            take_input("X", Board)
#         else:
#            take_input("O", Board)
#         counter += 1
#         if counter > 4:
#            tmp = check_win(Board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(Board)
#
# main(Board)

# input("Нажмите Enter для выхода!")

'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''



def press(file, result):
    with open(file, 'r', encoding='utf-8') as text:
        with open(result, 'w', encoding='utf-8') as res:
            inp_str = text.readline()
            ind = 0
            count = 1
            while ind < len(inp_str) - 1:
                if inp_str[ind] == inp_str[ind + 1]:
                    count += 1
                else:
                    if count == 1:
                        res.write(inp_str[ind])
                    else:
                        res.write(str(count) + inp_str[ind])
                    count = 1
                ind += 1

def depress(file, result):
    with open(file, 'r', encoding='utf-8') as text:
        with open(result, 'w', encoding='utf-8') as res:
            inp_str = text.readline()
            count = ''
            for letter in inp_str:
                if letter.isdigit():
                    count += letter
                else:
                    if count != '':
                        res.write(int(count) * letter)
                    else:
                        res.write(letter)
                    count = ''

press('file.txt','result.txt')
depress('result.txt','result2.txt')