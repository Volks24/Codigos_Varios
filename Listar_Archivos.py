# -*- coding: utf-8 -*-
import os


def mostrarContenidoCarpeta(carpeta):

	Arbol.write("--------------------------------------------------------\n")

	Arbol.write("   Carpeta: %s" % carpeta+"\n")

	Arbol.write("--------------------------------------------------------\n")

	archivos=carpetas=0

	for i in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,i)):

			Arbol.write(os.path.join(carpeta,i)+"\n")

			archivos+=1

		if os.path.isdir(os.path.join(carpeta,i)):

			carpetas+=1

	Arbol.write("\tarchivos: %s - carpetas: %s \n" % (archivos,carpetas))

	for i in os.listdir(carpeta):

		if os.path.isdir(os.path.join(carpeta,i)):

			mostrarContenidoCarpeta(os.path.join(carpeta,i))

 

carpetaInicio="./"
Arbol = open("Archivos.txt","w")
mostrarContenidoCarpeta(carpetaInicio)
Arbol.close()