import numpy as np
from builtins import enumerate

print('------------------------  EX - 1 ------------------------------------')
#Criar um intervalo de 3 zeros entre os números do Array
array1 = np.array([1, 2, 3, 4, 5])
zeros = np.zeros(len(array1) + (len(array1) - 1) * (3), dtype=int) #Zerando a Matriz e deixando com a quantidade necessaria
zeros[::4] = array1  #Pegando o array em um intevalo de 4 em 4 para substituir pelo array desejado
print(zeros)

print('------------------------  EX - 2 ------------------------------------')
#Criar um Array 8x8 com 0 e 1 intercalado
array2 = np.zeros((8, 8), dtype=int)
array2[1::2, ::2] = array2[::2, 1::2] = 1
print(array2)

print('------------------------  EX - 3 ------------------------------------')
#Função para trocar as posições das linhas
def changeline(l1,l2):
    m = np.array([[ 0,  1,  2,  3,  4],
                  [ 5,  6,  7,  8,  9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]])
    m[(l1,l2), :] = m[(l2,l1), :]
    print(m)

changeline(0,1)
changeline(2,3)

print('------------------------  EX - 4 ------------------------------------')
#Função para trocar as posições das colunas
def changecolumn(c1,c2):
    m = np.array([[ 0,  1,  2,  3,  4],
                  [ 5,  6,  7,  8,  9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]])
    m[:, (c1,c2)] = m[:, (c2,c1)]
    print(m)

changecolumn(2,3)
print('------------------------  EX - 5 ------------------------------------')
#Replicar o array de acordo com a quantidade de itens dele
array5 = np.array([1,2,3])
for x in range(len(array5) + 1):
    newa5 = np.array([array5])
    print(newa5)

print('------------------------  EX - 6 ------------------------------------')
#Formar uma Matriz com o Array
array6 = np.array([1,2,3])
new = np.repeat(array6, 3)
newa6 = new.reshape(3, 3)
print(newa6)

print('------------------------  EX - 7 ------------------------------------')
#Comando Where Numpy
array7 = np.array([4, 95, 37, 64, 42, 19, 55, 38, 46, 83, 48, 67, 98, 21, 10, 88])
where = (np.where((array7 > 34) & (array7 < 56)))
print(array7[where])

print('------------------------  EX - 8 ------------------------------------')
array8 = np.arange(0,101)
n = np.random.uniform(0,100)
dec = n - int(n)
print('Numero: {}'.format(n))
print('Inteiro mais próximo:')
if dec > 0.5:
    print(array8[int(n)] + 1)
else:
    print(array8[int(n)])

print('------------------------  EX - 9 ------------------------------------')
np.random.seed(100)
array9 = np.random.uniform(1, 50, 30)
print(array9)
for x, y in enumerate(array9):
    if y < 10:
        array9[x] = 10

    if y > 30:
        array9[x] = 30
print('---------- Array substituido ----------')
print(array9)

print('------------------------  EX - 10 ------------------------------------')
#Calcular o determinante segundo a regra(Formula) de Sarrus
array10 = np.arange(1,10)
matriz = array10.reshape(3, 3)
print(matriz)
aei = (matriz[0,0] * matriz[1,1] * matriz[2,2])
bfg = (matriz[0,1] * matriz[1,2] * matriz[2,0])
cdh = (matriz[0,2] * matriz[1,0] * matriz[2,1])
afh = (matriz[0,0] * matriz[1,2] * matriz[2,1])
bdi = (matriz[0,1] * matriz[1,0] * matriz[2,2])
ceg = (matriz[0,2] * matriz[1,1] * matriz[2,0])
det_mat = (aei + bfg + cdh) - (afh + bdi + ceg)
print('Determinante desta Matriz: {}'.format(det_mat))