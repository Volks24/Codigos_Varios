import pandas as pd
import numpy as np



Conver_Mat =  {"AA":[1,0], "GG":[0,1], "GA":[1,1], "AG":[1,1],"AA":[1,0], "CC":[0,1], "CA":[1,1], "AC":[1,1],"TT":[1,0], "GT":[1,1], "TG":[1,1],"CT":[1,1],"TC":[1,1],"--":[9,9],"":[9,9]}
Matriz_Datos = pd.read_csv (r'Datos/SNP_version.csv')
Matriz_Datos = Matriz_Datos.set_index("SNP Name")
nombres = list(Matriz_Datos.index) 

Matriz_Datos_Con = pd.DataFrame(index=range(0,Matriz_Datos.shape[0]*2), columns = Matriz_Datos.columns[:])
print (Matriz_Datos_Con)
pos = 0
for casos in nombres:
	print(pos)
	for j in range (0,Matriz_Datos.shape[1]):
		Conversion = Conver_Mat[Matriz_Datos.loc[casos][j]]
		Matriz_Datos_Con.loc[pos][j] = Conversion[0]
		Matriz_Datos_Con.loc[pos+1][j] = Conversion[1]
	pos = pos + 2
	
Matriz_Datos_Con.to_excel("Resultados/Converted.xlsx")
Matriz_Datos_Con.to_csv("Resultados/Converted.csv")

print(Matriz_Datos_Con)




