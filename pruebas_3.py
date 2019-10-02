import multiprocessing as mp
import pandas as pd
import numpy as np

def jaccard_similarity(x,y):
	# Compara Posicion a Posicion y devuelve el ratio entre True y el total de posiciones
	comparacion = np.char.equal(x,y)
	Pares_Identicos = np.sum(comparacion)
	return (Pares_Identicos/(len(comparacion)))
	
Matriz_Datos = pd.read_excel (r'Datos/Incognita_lite.xlsx', sheet_name='All data_789' )
Matriz_Datos = Matriz_Datos.set_index("SNP Name")

Vectores = []

for j in range (0,Matriz_Datos.shape[1]):
	Vectores.append(Matriz_Datos.iloc[:,j].tolist())

# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: `pool.apply` the `howmany_within_range()`

resultado_f = []

for i in range(0,Matriz_Datos.shape[1]-1):
	results = [pool.apply(jaccard_similarity, args=(Vectores[i], Vectores[j])) for j in range(i+1,Matriz_Datos.shape[1])]
	resultado_f.append(results)


# Step 3: Don't forget to close
pool.close()   

combinaciones = 0
for rows in resultado_f:
	print(len(rows))
	combinaciones = combinaciones + len(rows)
	print("\n")

print(combinaciones)
