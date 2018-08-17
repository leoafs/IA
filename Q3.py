import requests
from random import randint
def fitnes(antenas):
    aux= requests.get('http://localhost:8080/antenna/simulate?phi1={}&theta1={}&phi2={}&theta2={}&phi3={}&theta3={}'.format(antenas[0],antenas[1],antenas[2],antenas[3],antenas[4],antenas[5]))
    return float(aux.content.split()[0])
def popula(tamanho):
    antenas=[]
    for i in range(tamanho):
        antena = 6 * [0]

        antena[0]=randint(0,360)
        antena[1] = randint(0, 360)
        antena[2] = randint(0, 360)
        antena[3] = randint(0, 360)
        antena[4] = randint(0, 360)
        antena[5] = randint(0, 360)
        sinal=fitnes(antena)
        aux=[antena,sinal]
        antenas.append(aux)
    antenas.sort(key=lambda a:a[1],reverse=True)
    return  antenas
def sele(antenas):
    selecao=[]
    for i in range(2):
        a=randint(0,3)
        if a==0 or a==1:
            selecao.append(antenas[randint(0,len(antenas)//2)])
        else:
            selecao.append(antenas[randint(len(antenas)//2+1,len(antenas)-1)])

    return selecao
def cruzamento(selecao):
    filho1=[]
    filho2=[]
    for i in range(3):
        filho1.append(selecao[0][0][i])
    for i in range(3,6):
        filho1.append(selecao[1][0][i])
    filho1=mutar(filho1)
    for i in range(3):
        filho2.append(selecao[1][0][i])
    for i in range(3,6):
        filho2.append(selecao[0][0][i])
    filho2 = mutar(filho2)
    return filho1,filho2
def mutar(filho):
    i = randint(0,1)
    if i == 1:
        filho[4]+=3
    return filho
aux=popula(100)
filhos= []
for i in range(5):
    a=sele(aux)
    b=cruzamento(a)
    z=fitnes(b[0])
    aux2=[b[0],z]
    filhos.append(aux2)
    z = fitnes(b[1])
    aux3 = [b[1], z]
    filhos.append(aux3)
filhos.sort(key=lambda a:a[1],reverse=True)
print(filhos[0])
