#Integrantes: 192301-9 y 192462-2
import os

#Imprimimos donde estamos en la memoria
print(os.getcwd())

#Imprimimos una lista de lo que tenemos
print(os.listdir())

#Creamos 'modules'
os.mkdir('modules')

print(os.listdir())

#Nos cambiamos a la carpeta de module
os.chdir('modules')

#Creamos un documento txt
texto = open("README.txt", "x")
texto.write("Este es un archivo README")
texto.close()

#Imprimimos una lista de lo que tenemos
print(os.listdir())

#Imprimimos una las caracteristicas de el archivo
print(os.stat('README.txt'))

os.chdir('..')
print(os.getcwd())
print(os.listdir())


#Ruras de los archivos
archivo_c1 = "c1\\archivo_c1.txt"
archivo_c2 = "c2\\archivo_c2.txt"

#Rutas de destino
destino1 = "modules\\archivo_c1.txt"
destino2 = "modules\\archivo_c2.txt"

#Primera copia para el archivo_c1
if os.path.isfile(archivo_c1):
    os.system(f"copy {archivo_c1} {destino1}")
    print("Archivo copiado exitosamente.")
else:
    print(f"El archivo de origen '{archivo_c1}' no existe.")

#Segunda copia para el archivo_c2
if os.path.isfile(archivo_c2):
    os.system(f"copy {archivo_c2} {destino2}")
    print("Archivo copiado exitosamente.")
else:
    print(f"El archivo de origen '{archivo_c2}' no existe.")

#Nos cambiamos a la carpeta de module
os.chdir('modules')

#Renombramos los archivos
os.rename("archivo_c1.txt", "archivo_c1_copia.txt")
os.rename("archivo_c2.txt", "archivo_c2_copia.txt")

print(os.listdir())
os.chdir('..')
print(os.getcwd())

#Nos movemos a las carpetas C1 y C2 para leer el nombre de los archivos y eliminalos

os.chdir('c1')
print(os.listdir())
os.remove("archivo_c1.txt")
os.chdir('..')
os.chdir('c2')
print(os.listdir())
os.remove("archivo_c2.txt")

print("Fin del programa")