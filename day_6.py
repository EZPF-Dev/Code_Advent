# import fileinput

# string = []
# check = []
# count = 0
# count_2 = 0

# for letter in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day6.txt').readline():
#     string.append(letter)


# for item in string:
#     check.append(item)
#     count+=1
    
#     if len(check) == 4:
#         for char in check:
#              if check.count(char) > 1 :
#                  check.pop(0)
#                  count_2 = 0
#                  break
#              else:
#                 count_2 +=1
#                 if count_2 == 4:
#                     print ("found at:",count)
#                     print(char)
#                     break
                
                 
#PART 2
        
import fileinput

string = []
check = []
count = 0
count_2 = 0

for letter in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day6.txt').readline():
    string.append(letter)


for item in string:
    check.append(item)
    count+=1
    
    if len(check) == 14:
        for char in check:
             if check.count(char) > 1 :
                 check.pop(0)
                 count_2 = 0
                 break
             else:
                count_2 +=1
                if count_2 == 14:
                    print ("found at:",count)
                    print(char)
                    break
        



