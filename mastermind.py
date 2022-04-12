# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mastermind.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:24:22 by tomartin          #+#    #+#              #
#    Updated: 2022/04/12 15:39:46 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from aux import *

num = init_number()
answ = insert_nums()
total_answ = save_answ(answ)
check_nums(num, answ)
