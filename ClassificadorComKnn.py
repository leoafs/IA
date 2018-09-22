
import pandas as base
import numpy as np
from  sklearn.neighbors import KNeighborsClassifier
base = base.read_csv("C://Users//leona//Desktop//iris.csv")
x=np.array(base.drop('target',1))
y=np.array(base.target)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x,y)
print("Digite os seguintes parâmetros: Altura da Sépala,Largura da Sépala,Altura da pétala e Largura da pétala")
print()
alturaSepala=float(input())
larguradaSepala=float(input())
alturaPetala=float(input())
larguradaPetala=float(input())
print("Altura da Sépala:",alturaSepala)
print("Largura da Sépala:",larguradaSepala)
print("Altura da Pétala:",alturaPetala)
print("Largura da Pétala:",larguradaPetala)
aux=knn.predict([[alturaSepala,larguradaSepala,alturaPetala,larguradaPetala]])
print("A flor provavelmente é da classe:",aux[0])

alturaSepala=float(input())
print(knn.predict([[6.5,6.5,4.7,1.3]]))
