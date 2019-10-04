import pandas as pd
import numpy as np

from time import time

def jaccard_similarity(x,y):
	# Compara Posicion a Posicion y devuelve el ratio entre True y el total de posiciones
	comparacion = np.char.equal(x,y)
	Pares_Identicos = np.sum(comparacion)
	return (Pares_Identicos/(len(comparacion)))

t1 = time()

Matriz_Datos = pd.read_excel (r'Datos/Incognita.xlsx', sheet_name='All data_789' )

Jaccard_Matriz = pd.DataFrame(index=Matriz_Datos.columns[1:], columns = Matriz_Datos.columns[1:])
Indice_Jaccard = []
	

for x in range(1,(Matriz_Datos.shape[1]-1)):
	indice_col2 = x + 1
	for y in range (indice_col2,Matriz_Datos.shape[1]):
		print ("Col 1:"+str(x))
		indice_J =jaccard_similarity(Matriz_Datos.iloc[:,x].tolist(), Matriz_Datos.iloc[:,y].tolist()) # [: (Toda la coluna) , Columna ]
		Indice_Jaccard.append(indice_J) # Valor de similitud Para Cada Par
		Jaccard_Matriz.loc[Matriz_Datos.columns.values[x], Matriz_Datos.columns.values[y]] = indice_J
		
Jaccard_Matriz.fillna("-" , inplace = True)
Jaccard_Matriz.to_excel("Distancias_Jaccard.xlsx")
del Jaccard_Matriz

print (time() - t1)