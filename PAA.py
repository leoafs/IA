def justificar(palavras,largura):
  matrizC=len(palavras)*[len(palavras)*[-1]]
  for i in range(len(palavras)):
    matrizC[i][i] = largura-len(palavras[i])
    for j in range(i+1,len(palavras)):
      matrizC[i][j] = matrizC[i][j-1]-len(palavras[j])-1
  for i in range(len(palavras)):
    for j in range(i,len(palavras)):
      if matrizC[i][j]<0:
        matrizC[i][j]=10**30
      else:
        matrizC[i][j] = (matrizC[i][j])**2
  custoM=len(palavras)*[-1]
  resultado=len(palavras)*[-1]
  for i in range(len(palavras)-1,-1,-1):
    custoM[i]=matrizC[i][len(palavras)-1]
    resultado[i]=len(palavras)

    for j in range(len(palavras)-1,i,-1):
      if matrizC[i][j-1]==10**30:
       pass
      if custoM[i]>custoM[j]+matrizC[j][j-1]:
       custoM[i]=custoM[j] + matrizC[i][j-1]
       resultado[i]=j
  x=0
  y=0
  aux=''
  y = resultado[i]
  for k in range(x,y):
    aux+=palavras[k]+" "
  aux+="\n"
  x=y
  while y<len(palavras):
    y = resultado[i]
    for k in range(x,y):
      aux+=palavras[k]+" "
    aux+="\n"
    x=y
  return aux
palavra1=["Writing", "e-mails", "is" ,"fun",",", "and", "with", "this", "program",",",
"they", "even" ,"look" ,"nice."]
a=justificar(palavra1,11)
print(a)
