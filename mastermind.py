# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mastermind.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:24:22 by tomartin          #+#    #+#              #
#    Updated: 2022/04/11 17:34:31 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from aux import *

num = init_number()
answ = insert_nums()
print (num, answ)
check_nums(num, answ)
