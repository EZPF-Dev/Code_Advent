#  [H]                 [Z]         [J]
#  [L]     [W] [B]     [G]         [R]
#  [R]     [G] [S]     [J] [H]     [Q]
#  [F]     [N] [T] [J] [P] [R]     [F]
#  [B]     [C] [M] [R] [Q] [F] [G] [P]
#  [C] [D] [F] [D] [D] [D] [T] [M] [G]
#  [J] [C] [J] [J] [C] [L] [Z] [V] [B]
#  [M] [Z] [H] [P] [N] [W] [P] [L] [C]
#   1   2   3   4   5   6   7   8   9 

# import fileinput
# from shutil import move, register_archive_format
# stack_1 = ['M','J','C','B','F','R','L','H']
# stack_2 = ['Z','C','D']
# stack_3 = ['H','J','F','C','N','G','W']
# stack_4 = ['P','J','D','M','T','S','B']
# stack_5 = ['N','C','D','R','J']
# stack_6 = ['W','L','D','Q','P','J','G','Z']
# stack_7 = ['P','Z','T','F','R','H']
# stack_8 = ['L','V','M','G']
# stack_9 = ['C','B','G','P','F','Q','R','J']

# stack_list={'1':stack_1, '2':stack_2, '3':stack_3, '4':stack_4, '5':stack_5, '6':stack_6, '7':stack_7, '8':stack_8, '9':stack_9}

# for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day5.txt'):
#     task = line.split()
#     stack= task[1]
#     sender=task[3]
#     receiver=task[5]
#     stack_list[sender]
#     for i in range(0,-abs(int(stack)),-1):
#         stack_list[receiver].append(stack_list[sender][-1])
#         stack_list[sender].pop(-1)

# print(stack_list['1'][-1], stack_list['2'][-1], stack_list['3'][-1], stack_list['4'][-1], stack_list['5'][-1], stack_list['6'][-1], stack_list['7'][-1], stack_list['8'][-1], stack_list['9'][-1])


""" stack_1 = ['M','J','C','B']
stack_2 = ['G','M','V','D','C','Z']
stack_3 = ['H','J','F','C']
stack_4 = ['P','J','D','M','T','S','B','Z','G','J','P','Q','D','L','W','L']
stack_5 = ['N','C','D','R','J','H','R','F','W','G']
stack_6 = []
stack_7 = ['P','Z','T']
stack_8 = ['N','H','L','R','F']
stack_9 = ['C','B','G','P','F','Q','R','J'] """

# Part 2

import fileinput
from shutil import move, register_archive_format
stack_1 = ['M','J','C','B','F','R','L','H']
stack_2 = ['Z','C','D']
stack_3 = ['H','J','F','C','N','G','W']
stack_4 = ['P','J','D','M','T','S','B']
stack_5 = ['N','C','D','R','J']
stack_6 = ['W','L','D','Q','P','J','G','Z']
stack_7 = ['P','Z','T','F','R','H']
stack_8 = ['L','V','M','G']
stack_9 = ['C','B','G','P','F','Q','R','J']

stack_list={'1':stack_1, '2':stack_2, '3':stack_3, '4':stack_4, '5':stack_5, '6':stack_6, '7':stack_7, '8':stack_8, '9':stack_9}

for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day5.txt'):
    task = line.split()
    stack= task[1]
    sender=task[3]
    receiver=task[5]
    stack_list[sender]
    for i in range(-abs(int(stack)),0,1):
        stack_list[receiver].append(stack_list[sender][i])
        stack_list[sender].pop(i)

print(stack_list['1'][-1], stack_list['2'][-1], stack_list['3'][-1], stack_list['4'][-1], stack_list['5'][-1], stack_list['6'][-1], stack_list['7'][-1], stack_list['8'][-1], stack_list['9'][-1])
#print(stack_list['1'][-1], stack_list['2'][-1], stack_list['3'][-1], stack_list['4'][-1], stack_list['5'][-1], stack_list['7'][-1],stack_list['9'][-1])

""" stack_1 = ['M','J','C','B','F','R','L','H','Z','C','D']
stack_2 = ['L','V','M','G']
stack_3 = ['H','J','F','C','N','G','W']
stack_4 = ['P','J','D','M','T','S','B', 'W','L','D','Q','P','J','G','Z']
stack_5 = ['N','C','D','R','J']
stack_6 = []
stack_7 = ['P','Z','T','F','R','H']
stack_8 = []
stack_9 = ['C','B','G','P','F','Q','R','J']
 """