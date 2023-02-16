import fileinput


def inventario():
 inv=[]
 elfos=[]
 i=0
 calorias = 0
   
 for line in fileinput.input(files ='calorias.txt'):
     if line == '\n' :
        #elfos.append(calorias) 
        inv.append(calorias) 
        calorias = 0
        elfos=[]
     else:
      calorias = calorias + int (line) 
 return inv

def elfo_mas_calorias (inventario):
  elfo_mas = 0
  for elfo_actual in inventario:
    if elfo_actual > elfo_mas:
     elfo_mas = elfo_actual 

  return elfo_mas

def top_3_elfos (elfo_mas, inventario):
  elfo_1 = elfo_mas
  elfo_2 = 0
  elfo_3 = 0
  for elfo_actual in inventario:
    if elfo_1 > elfo_actual > elfo_2:
      elfo_2 = elfo_actual

    if elfo_2 > elfo_actual > elfo_3:
      elfo_3 = elfo_actual

  print ('top 3 elfos',elfo_1, elfo_2, elfo_3)
  ans = elfo_1 + elfo_2 + elfo_3
  return ans
         
inv = inventario()
elfo_mas = elfo_mas_calorias(inv)
ans = top_3_elfos (elfo_mas, inv)   
print (ans)