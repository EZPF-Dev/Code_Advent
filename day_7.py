import fileinput
from treelib import Node, Tree
import pdb
count = 0
current_dir = []
dir = []
tree = Tree()

def map_dir(input:str):
   for line in fileinput.input(files = input):
      line = line.split()
      if line[0] == '$':
         if line [1] == 'cd':
            if line [2] == '..':
               current_dir.pop()
            else:
                if len(current_dir) == 0:
                    tree.create_node(str(line[2]),str(line[2]), data= dir)
                    current_dir.append(line[2])
                else:
                     current_dir.append(line[2])
      elif line[1] == 'ls':
            continue
      elif line[0] == 'dir':
         tree.create_node(tag=line[1],identifier=line[1],data="dir", parent=current_dir[-1])
      else:
           tree.create_node(tag=line[1],identifier=line[1],data={"tamaño":line[0]},parent=current_dir[-1])
   return tree.to_dict(with_data=True)

print(map_dir('C:/Users/eee5ga/Desktop/Code/Code_Advent/Inputs/day7test.txt'))


