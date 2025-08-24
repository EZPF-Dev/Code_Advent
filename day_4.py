# #Part one
# import fileinput
# pairs = []
# count = 0
# for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day4.txt'):
    
#     pairs = line.strip().split(",")
#     f_pair = pairs[0].split("-")
#     s_pair = pairs[1].split("-")
    
#     if int(f_pair[0]) <= int(s_pair[0]) <= int(f_pair[1]) and int(f_pair[0]) <= int(s_pair[1]) <= int(f_pair[1]):
#         count +=1
#         print (pairs,"yes")
#     elif int(s_pair[0]) <= int(f_pair[0]) <= int(s_pair[1]) and int(s_pair[0]) <= int(f_pair[1]) <= int(s_pair[1]):
#         count +=1
#         print (pairs,"yes")

     
# print (count)

import fileinput
pairs = []
count = 0
for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day4.txt'):
    
    pairs = line.strip().split(",")
    f_pair = pairs[0].split("-")
    s_pair = pairs[1].split("-")
    
    if int(f_pair[0]) <= int(s_pair[0]) <= int(f_pair[1]) and int(f_pair[0]) <= int(s_pair[1]) <= int(f_pair[1]):
        count +=1
        print (pairs,"yes")
    elif int(s_pair[0]) <= int(f_pair[0]) <= int(s_pair[1]) and int(s_pair[0]) <= int(f_pair[1]) <= int(s_pair[1]):
        count +=1
        print (pairs,"yes")
    elif int(f_pair[0]) <= int(s_pair[0]) <= int(f_pair[1]) and int(f_pair[0]) <= int(s_pair[1]) >= int(f_pair[1]):
        count +=1
        print (pairs,"yes")
    elif int(s_pair[0]) <= int(f_pair[0]) <= int(s_pair[1]) and int(s_pair[0]) <= int(f_pair[1]) >= int(s_pair[1]):
        count+=1
        print (pairs,"yes")
    else:
        print (pairs,"no")


print (count)