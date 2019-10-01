import multiprocessing as mp
import pandas as pd
import numpy as np

def jaccard_similarity(x,y,data):
	# Compara Posicion a Posicion y devuelve el ratio entre True y el total de posiciones
	vector_1 = data.iloc[:,x].tolist()
	vector_2 = data.iloc[:,y].tolist()
	comparacion = np.char.equal(vector_1,vector_2)
	Pares_Identicos = np.sum(comparacion)
	return (Pares_Identicos/(len(comparacion)))

Datos = pd.read_excel (r'Datos/Incognita_lite.xlsx', sheet_name='All data_789' )


#print (Datos.shape[0])
#print (Datos.shape[1]) ### Columnas

pool = mp.Pool(processes=4)

results = [pool.apply(jaccard_similarity, args=(Datos.iloc[:,z],Datos.iloc[:,z+1],Datos)) for z in range(0,10)]

print(results)

