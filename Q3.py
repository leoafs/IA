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
def cruzamento(selecao,tamanho):
    filho1=[]
    filho2=[]
    for i in range(3):
        filho1.append(selecao[0][0][i])
    for i in range(3,6):
        filho1.append(selecao[1][0][i])
    for i in range(3):
        filho2.append(selecao[1][0][i])
    for i in range(3,6):
        filho2.append(selecao[0][0][i])


    return filho1,filho2

aux=popula(10)
a=sele(aux)
print(a)
print(cruzamento(a,10))
