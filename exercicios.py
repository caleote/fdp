'''from math import *

def perimetro(r):
    perimetro=2*r*pi
    return perimetro


def area(r):
    area=pi*(r**2)
    return area


r=int(input('diz o raio do circulo'))
print(perimetro(r))
print(area(r)

def areaq(l):
    areaq=l*l
    return areaq
def perimetroq(l):
    perimetroq = 4*l
    return perimetroq

l=int(input('lado do quadrado : '))
print('area = ',areaq(l))
print('perimetro=', perimetroq(l))

l=int(input('lado e raio'))
print(areaq(l), area(l))


def load_data(fname):
    data = open(fname, "r")
    return data


def espaco(fname):
    data = load_data(fname)
    content = data.read()
    i = 0
    espacos = 0
    for i in range(0, len(content)):
        if content[i] == (' '):
            espacos += 1
    return espacos


def palavra(fname):
    data = load_data(fname)
    content = data.read()
    if content[-1] == (' '):
        palavras = espaco(fname)
    else:
        palavras = espaco(fname) + 1
    return palavras

espacos = espaco("martim.txt")
palavras = palavra ("martim.txt")
print ("espacos:", espacos)
print ("palavras:", palavras)

def load_data(fname):
    data=open(fname, 'r')
    return data

def branco(fname):
    data=load_data (fname)
    content= data.read()
    branco=0
    palavra=0
    for i in fname:
        if content[i]==(' '):
            branco +=1
        else:
            palavra += 1

brancos = branco("martim.txt")
palavras = palavra ("martim.txt")
print ("espacos:", branco)
print ("palavras:", palavra)'''

'''
famous_quote = 'Há limites para aquilo que o POVO português pode aguentar.'

for i in range(1, len(famous_quote)):
    if i%2 == 0:
        famous_quote = famous_quote[:i] + '2' + famous_quote[i+1:]
print (famous_quote)
'''

def get_min(l):
    '''
    O programa recebe uma lista de inteiros e devolve o maior número existente na lista.
    @requires l uma lista de inteiros
    @ensures o número máximo que existe na lista
    '''

    return min(l)


lista = list(input("Insira a lista:"))
print('Maior:', get_min(lista))