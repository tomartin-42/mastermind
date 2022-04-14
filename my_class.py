# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    class.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/11 16:03:32 by tomartin          #+#    #+#              #
#    Updated: 2022/04/14 16:00:25 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
class IncorrectValue(Exception):
    pass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

