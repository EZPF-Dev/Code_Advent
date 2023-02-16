import fileinput

def strategy ():
    elfos = []
    yo = []
    for line in fileinput.input(files ='estrategia.txt'):
        
           elfos.append(line[:1])
           yo.append(line[2:-1])
    return elfos, yo

def match_1 (elfos, yo):
    score = 0
    equiv = {'X':1,'Y':2, 'Z':3}
    punct = {'Win':6, 'Tie':3, 'Lose':0}
    
    for (x,y) in zip(elfos,yo):
        
        if  x == "A" and y == "X":
            score = score + punct.get('Tie')+  equiv.get(y)

        if x == "A" and y == "Y":
            score = score + punct.get('Win')+  equiv.get(y)  

        if x == "A" and y == "Z":
            score = score + punct.get('Lose')+  equiv.get(y)

        if x == "B" and y == "X":
            score = score + punct.get('Lose')+  equiv.get(y)

        if x == "B" and y == "Y":
            score = score + punct.get('Tie')+  equiv.get(y)   

        if x == "B" and y == "Z":
            score = score + punct.get('Win')+  equiv.get(y)

        if x == "C" and y == "X":
            score = score + punct.get('Win')+  equiv.get(y)

        if x == "C" and y == "Y":
            score = score + punct.get('Lose')+  equiv.get(y)   

        if x == "C" and y == "Z":
            score = score + punct.get('Tie')+  equiv.get(y)
            
    return score

def match_2 (elfos, yo):
    score = 0
    equiv = {'X':1,'Y':2, 'Z':3}
    punct = {'Win':6, 'Tie':3, 'Lose':0}
    
    for (x,y) in zip(elfos,yo):
        
        if  x == "A" and y == "X":
            score = score + punct.get('Lose')+  equiv.get('Z')

        if x == "A" and y == "Y":
            score = score + punct.get('Tie')+  equiv.get('X')  

        if x == "A" and y == "Z":
            score = score + punct.get('Win')+  equiv.get('Y')

        if x == "B" and y == "X":
            score = score + punct.get('Lose')+  equiv.get('X')

        if x == "B" and y == "Y":
            score = score + punct.get('Tie')+  equiv.get('Y')   

        if x == "B" and y == "Z":
            score = score + punct.get('Win')+  equiv.get('Z')

        if x == "C" and y == "X":
            score = score + punct.get('Lose')+  equiv.get('Y')

        if x == "C" and y == "Y":
            score = score + punct.get('Tie')+  equiv.get('Z')   

        if x == "C" and y == "Z":
            score = score + punct.get('Win')+  equiv.get('X')
            
    return score



elfos,yo=strategy()
#total=match_1(elfos,yo)
total=match_2(elfos,yo)

print (total)
