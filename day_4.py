import fileinput
pairs = []
for line in fileinput.input(files ='C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day4.txt'):
    pairs = line.split(",")
    print (pairs)