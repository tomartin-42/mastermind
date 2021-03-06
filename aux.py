# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aux.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 15:19:41 by tomartin          #+#    #+#              #
#    Updated: 2022/04/14 16:20:01 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randrange
import my_class

#Generate random code
def init_number(leng_num):
    secret_num = []
    i = int()

    while i < leng_num:
        secret_num.append(int(randrange(10)))
        i = i + 1
    return secret_num

#Insert and parse answers
def insert_nums(answ_num):
    insert_num = []
    i = int()

    while i < answ_num:
        while True:
            print ("Inserte el", i + 1, "num =")
            num = input()
            try:
                num = int(num)
                if (num < 0 or num > 9):
                    raise my_class.IncorrectValue
            except ValueError:
                print ("Num required")
            except my_class.IncorrectValue:
               print ("> 0 or < 10")
               pass
            else:
                insert_num.append(num)
                break
        i = i + 1
    print ("Insert num", insert_num)
    return insert_num

#Check if the number(only one aswer number) is in secret num
#or not, print the answer 
def check_incl(answ, nums):
    i = 0
    flag = False

    for x in nums:
        if (x == answ):
            print (my_class.bcolors.WARNING + str(answ), " " + my_class.bcolors.ENDC, end="")
            flag = True
            break
    if (flag == False):
        print (my_class.bcolors.ENDC + str(answ), " ", end="")

#Check if is correct number in correct position
#if is not correct pass to check_incl function
def check_nums(num, answ):
    i = 0
    finish = int(0)

    for x in num:
        if (x == answ[i]):
            print (my_class.bcolors.OKGREEN + str(answ[i]), " " + my_class.bcolors.ENDC, end="")
            finish += 1
        else:
            check_incl(answ[i], num)
        i = i + 1
    return finish
