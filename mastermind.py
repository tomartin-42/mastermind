# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mastermind.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:24:22 by tomartin          #+#    #+#              #
#    Updated: 2022/04/14 16:01:22 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from aux import *

total_answ = []
leng_num = int(5)
answ_try = int(5)
v = 0
i = 0
while v == 0:
    try:
        aux = input("Inseter secret num len ")
        leng_num = int(aux)
        aux = input("Insert num trys ")
        answ_try = int(aux)
        v = 1
    except ValueError:
        print("Incorrect value")
        v = 0
answ_num = leng_num
num = init_number(leng_num)
while i < answ_try:
    answ = insert_nums(answ_num)
    total_answ.append(answ)
    for answ in total_answ:
        finish = check_nums(num, answ)
        print()
    i = i + 1
    if finish == leng_num:
        print("Congratulation!!! the number is ", num) 
        quit()
print("Sorry!! You don't find the secret number :(")
