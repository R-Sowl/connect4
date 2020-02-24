 def grille_vide():#Ivane
  gril={}
  for i in range(6):#lignes
    for j in range(7):#colonnes
      gril[(i,j)]=0
  return(gril)
  
def affiche(gril):#Lucas
  print("""
    0 1 2 3 4 5 6
   ---------------""",end='')
  
  for i in range(5,-1,-1):#lignes
    print('\n',i,'|',end='')#!pour chaque ligne
    for j in range(7):#colonnes
      if gril[(i,j)]==0:#teste si la case est vide
        print('.|',end='')#si c'est le cas alors il affiche un "."
      elif gril[(i,j)]==1:#teste si la case est rempli par le joueur 1
        print('x|',end='')#si c'est le cas alors il affiche un "x"
      elif gril[(i,j)]==2:#teste si elle est rempli par le joueur 2
        print('0|',end='')#si c'est le cas il affiche  un "x"
  print('''
   ---------------''')

def coup_possible(gril,col):#Ivane
  for i in range(6):
    if gril[(i,col)]==0:
      return True
  return False

def jouer(gril,j,col):#Ivane
  if coup_possible(gril,col)==True:#s'il est possible de jouer dans la colonne choisie
    for i in range(6):#pour chaque ligne
      if gril[(i,col)]==0:#si la case est vide
        gril[(i,col)]=j#on affecte la valeur du joueur
        affiche(gril)#on fait la fonction
        return
  else:
    print("impossible de jouer dans cette colonne")
    return
  
def vert(gril,lig,col):#Ivane
  if lig>=3:
    for j in range(lig,lig-4,-1):
      if gril[(lig,col)]!=gril[(j,col)]:
        return False#attention qd cest vide!!!
    return True
  else:
    return False

def horiz(gril,lig,col):#Lucas OK
  if col>=3:
    for i in range(col-1,col-4,-1):
      if gril[(lig,col)]!=gril[(lig,i)]:
        return False
  if col<=3:
    for i in range(col+1,col+4,1):
      if gril[(lig,col)]!=gril[(lig,i)]:
        return False
  return True

def diag_bas(gril,lig,col):#Lucas
  if lig>2:
    if col<=3:
      for i in range(lig,lig-4,-1):
        if gril[(lig,col)]!=gril[(i,i+2)]:
          return False
        return True
    if col>=3:
      for i in range(lig,lig-4,-1):
        if gril[(lig,col)]!=gril[(i,i-2)]:
          return False
        return True
  else:
    return False     

def diag_haut(gril,lig,col):#Ivane OK
  col2=col
  if lig<3:#parce qu'on monte
    if col<=3:
      for i in range(lig+1,lig+4):
        if gril[(lig,col)]!=gril[(i,i+(col-lig))]:
          result=False
      result=True
    if col>=3:
      for i in range(lig+1,lig+4):
        col2=col2-1
        if gril[(lig,col)]!=gril[(i,col2)]:#!
          result=False
      result=True
  else:
    result=False
  return result


'''#les tests
grilleTest={(i,j):0 for i in range(6) for j in range(7)}
for i in range(4):
  grilleTest[(0,i+2)]=1
  grilleTest[(i+1,2)]=2
for i in range(1,5):
  grilleTest[(i,i-1)]=1
affiche(grilleTest)
grilleTest[(0,3)]=1
grilleTest[(1,4)]=1
grilleTest[(2,5)]=1
grilleTest[(3,6)]=1

grilleTest[(2,2)]=2
grilleTest[(1,3)]=2
grilleTest[(3,1)]=2
grilleTest[(4,0)]=2
affiche(grilleTest)

print(diag_haut(grilleTest,1,3))
print(diag_haut(grilleTest,0,3))'''
