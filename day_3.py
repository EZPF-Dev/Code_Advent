import fileinput
# PART 1
def half ():
    sum = 0
    for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day3.txt'):
        res_first, res_second = line[:len(line)//2], line[len(line)//2:]
        for letter in res_first:
            if res_second.count(letter) > 0:
                if letter.islower() == True:
                    sum += ord(letter)-96
                    break
                else:
                    sum += ord(letter)-38
                    break
    return sum

#print(half())

#PART 2
def badge ():
    count = 0
    sum2 = 0
    list = []
    for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day3.txt'):
        count +=1
        list.append(line)
        if count % 3 == 0:
            for letter in list[0]:   
                if list[1].count(letter) > 0 and list[2].count(letter) > 0:
                    if letter.islower() == True:
                        print (letter)
                        sum2 += ord(letter)-96
                        break
                    else:
                        print(letter)
                        sum2 += ord(letter)-38
                        break     
            list = []
    return sum2            

print(badge())

            

        
        
        
        
        