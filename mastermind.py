# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mastermind.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:24:22 by tomartin          #+#    #+#              #
#    Updated: 2022/04/13 15:49:50 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from aux import *

total_answ = []
leng_num = int(8)
answ_num = leng_num
answ_try = int(5)
i = int(0)

num = init_number(leng_num)
while i < answ_try:
    answ = insert_nums(answ_num)
    total_answ.append(answ)
    for answ in total_answ:
        check_nums(num, answ)
        print()
    i = i + 1
