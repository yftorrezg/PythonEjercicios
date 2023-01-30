""" 
Unir muchos, unos 1000 archivos de python en uno solo que se llamara fer.py

ejemplo:
ex001_version.py
ex002_print.py
...
ex999_ordenar_lista_cadenas_segun_longitud_cadena.py
"""

# Importar módulos
import os
import glob

 # Variables
ruta = "./Parte001"
archivos = glob.glob(os.path.join(ruta, "ex*.py"))
salida = "fer.py"

# Unir archivos 
with open(salida, "w") as f_out:
    for archivo in archivos:
        with open(archivo) as f_in:
            f_out.write(f_in.read())
            f_out.write("")

 # Salida
print("Archivos unidos en: {}".format(salida))

# Archivos unidos en: fer.py

# Path: Parte001\ex1001_unir_archivos_python.py