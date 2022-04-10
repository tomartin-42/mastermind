# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aux.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 15:19:41 by tomartin          #+#    #+#              #
#    Updated: 2022/04/10 17:33:15 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randrange

#Generate random code
def init_number():
    secret_num = []
    for i in range(5):
        secret_num.append(randrange(10))
    print(secret_num)
    return init_number

def insert_nums():
    insert_num = []
    for i in range(1,6):
        while True:
            print ("Inserte el", i, "num =")
            num = input()
            try:
                num = int(num)
            except ValueError:
                print ("Num required")
            else:
                insert_num.append(num)
                break
    print ("Insert num", insert_num)
