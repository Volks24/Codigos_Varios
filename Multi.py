import multiprocessing as mp
import pandas as pd
import numpy as np

def jaccard_similarity(x,y , v_1 , v_2):
	# Compara Posicion a Posicion y devuelve el ratio entre True y el total de posiciones
	comparacion = np.char.equal(x,y)
	Pares_Identicos = np.sum(comparacion)
	return ((Pares_Identicos/(len(comparacion))), v_1 , v_2)
	

t1 = time()


Matriz_Datos = pd.read_excel (r'Datos/Incognita_lite.xlsx', sheet_name='All data_789' )




### Preparacion Datos

Vectores = []

for j in range (0,Matriz_Datos.shape[1]):
	Vectores.append(Matriz_Datos.iloc[:,j].tolist())

Jaccard_Matriz = pd.DataFrame(index=Matriz_Datos.columns[1:], columns = Matriz_Datos.columns[1:])




# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: `pool.apply` the `howmany_within_range()`

resultado_f = []

for v_1 in range(0,Matriz_Datos.shape[1]-1):
  v_2 = v_1 + 1
  results = [pool.apply(jaccard_similarity, args=(Vectores[v_1], Vectores[j] ,v_1 , j ) ) for j in range(v_2,Matriz_Datos.shape[1])]
  for k in range(0,len(results)):
    Jaccard_Matriz.loc[results[k][2] , results[k][1]] = results[k][0]
  resultado_f.append(results) # Borrar

		

# Step 3: Don't forget to close
pool.close()   

Jaccard_Matriz.fillna("-" , inplace = True)
Jaccard_Matriz.to_excel("Distancias_Jaccard.xlsx")


print (time() - t1)


combinaciones = 0
for rows in resultado_f:
	print(len(rows))
	combinaciones = combinaciones + len(rows)
	print("\n")

# print(combinaciones)
# print(results)
# print(results[0])
# print(results[0][0])
# print(results[0][1][0])

# print (resultado_f[0])