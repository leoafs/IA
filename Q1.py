raiz=[3,3,1,None]
arvore=[]
arvore.append(raiz)
def ida(i):
    if arvore[i][0]==3 and arvore[i][1]==3:
        arvore.append([2,2,0,i])
        arvore.append([3,1,0,i])
    elif arvore[i][0] == 2 and arvore[i][1] == 2:
        arvore.append([0, 2, 0, i])
    elif arvore[i][0] == 0 and arvore[i][1] == 3:
        arvore.append([0, 1, 0, i])
    elif arvore[i][0] == 1 and arvore[i][1] == 1 or arvore[i][0] == 0 and arvore[i][1] == 2:
        arvore.append([0, 0, 0, i])
        return 1
    elif arvore[i][0]>arvore[i][1]:

        if arvore[i][0]==2:
            arvore.append([1,0,0,i])


        elif arvore[i][0]==3 and arvore[i][1]==2:
            arvore.append([3, 0, 0, i])
        elif arvore[i][0]==3 and arvore[i][1]==1:
            arvore.append([1, 1, 0, i])

def volta(i):
    if arvore[i][0] == 3 and arvore[i][1] == 1:
        arvore.append([3, 2, 1,i])
    elif arvore[i][0] == 3 and arvore[i][1] == 0:
        arvore.append([3, 1, 1,i])
    elif arvore[i][0] ==1 and arvore[i][1]==1:
        arvore.append((2, 2, 1,i))
    elif arvore[i][0] == 0 and arvore[i][1] == 2:
        arvore.append((0, 3, 1, i))
    elif arvore[i][0] == 0 and arvore[i][1] == 1:
        arvore.append((1, 1, 1, i))
        arvore.append((0, 2, 1, i))
def buscaEmLArgura(arvore):
    for i in range(len(arvore)):
        if arvore[i][0]==0 and arvore[i][1]==0:
            print(arvore[i],'<-',end='')
            while True:
                if i==0:
                    break
                print(arvore[arvore[i][3]],'<-',end='')

                i=arvore[i][3]

            break
i=0
while True:
    if arvore[i][2]==1:
        a=ida(i)
    else:
        print(i)
        volta(i)
    i+=1
    if a==1:
        break

buscaEmLArgura(arvore)
