import random
from Game_in_Candy import Game, Assign_names, Assign_names_game_with_bot, Game_with_bot
from Tic_Tac_Toe import Game_tic_tac_toe
from Parse_RLE import Parse_back_RLE, Parse_RLE
# 1.) Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_str = 'абв арыпа абвоарво рсыумым провабв'.split()
# for i in my_str:
#     if i.find('абв') != -1:
#         my_str.remove(i)
# print(*my_str)




# 2.) Создайте программу для игры с конфетами человек против человека.

#     Условие задачи: 
#     На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#     Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \
#     Все конфеты оппонента достаются сделавшему последний ход. 
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?



# name_second_player = input('Имя второго игрока: ')
# Assign_names(name_first_player, name_second_player)
# Game()


#  a) Добавьте игру против бота

# name_player = input('Имя игрока: ')
# Assign_names_game_with_bot(name_player)
# Game_with_bot()

#  b) Подумайте как наделить бота ""интеллектом""

# скорее всего тут надо что бы в конце от 100 примерно бот перестал вводить рандомные числа , 
# а старался вводить что-бы они были менее 29

# 3.) Создайте программу для игры в ""Крестики-нолики"".

# print('Игра Крестики-нолики\n')
# Game_tic_tac_toe()

#4.) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

try:
    input_file = 'input_data.txt'
    output_file = 'output_data.txt'
    with open(input_file, 'r') as inp: 
        big_num = inp.read().split()
    for i in range(len(big_num)):
        with open(output_file, 'a') as outp:
            outp.write(Parse_RLE(big_num[i]))
            outp.write('\n')
    with open(output_file, 'r') as outp:
        small_num = outp.read().split()
    with open(input_file, 'w') as inp:
        inp.write('')
    for i in range(len(small_num)):
        pt = ''
        net_num = pt + str(Parse_back_RLE(small_num[i]))
        with open(input_file, 'a') as inp:
            inp.write('\n')
            inp.write(net_num)
            inp.write(' ')    
except ValueError:
    print('Упс.Что-то пошло не так(((Попробуй еще раз!')


# 5.) Входные и выходные данные хранятся в отдельных текстовых файлах.




