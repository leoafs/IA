raiz=[3,3,1]
arvore=[]
arvore.append(raiz)

def ida(i):

        if arvore[i][0]==3 and arvore[i][1]==3:
            arvore.append([1,1,0])
            arvore.append([3,1,0])
            arvore.append([1,3,0])
        elif arvore[i][1]>arvore[i][0]:
            arvore.append((-1,-1,-1))

        elif arvore[i][0]>arvore[i][1]:
            if arvore[i][0]==3 and arvore[i][1]==2:
                arvore.append([2,1,0])
                arvore.append([1,2,0])
                arvore.append([3,0,0])
            elif arvore[i][0]==2:
                arvore.append([1,0,0])
                return 0
            elif arvore[i][0]==1:
                arvore.append([0,0,0])
                return 1
        elif arvore[i][0]==2 and arvore[i][1]==2:
            arvore.append([1,1,0])
            arvore.append([2,0,0])
            arvore.append([0,2,0])
            return 0
        else:
            arvore.append([-1,-1,-1])

def volta(i):
    if arvore[i][0] == 3 and arvore[i][1] == 1:
        arvore.append([3, 2, 1])
    elif arvore[i][0] ==2 and arvore[i][1]==2:
        arvore.append((3, 2, 1))
        arvore.append((2,3,1))
    elif arvore[i][0]<arvore[i][1]:
        arvore.append([-1,-1,-1])
i=0
while True:
    ida(i)

    for s in range(i+1,len(raiz)):
        volta(s)

print(arvore)
