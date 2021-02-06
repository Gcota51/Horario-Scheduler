# Horario-Scheduler

Integrantes:
- Cota Martínez Guillermo Oswaldo
- Macías Gómez Jorge

Este es el repositorio para el proyecto de la asignatura Matemáticas Discretas y Análisis de Algoritmos de la Licenciatura en Ciencia de Datos del Instituto de Investigaciones en Matemáticas Aplicada y Sistemas de la UNAM.

El objetivo de este proyecto es el de hacer un análisis sobre los horarios de la Facultad de Ciencias de la UNAM durante el semestre 2021-1 y con base al plan de estudios académicos de la Licenciatura de Matemáticas (en proceso de revisión si se amplía a más carreras), sugerir horarios para los estudiantes según su avance e intereses en materias optativas.

El presente proyecto está dividido en distintas partes que para la comprensión del lector se describen a continuación:

El documento en PDF trae las documentaciones técnica y ejecutiva del caso.

Para los programas, se pueden leer de dos maneras: Leyendo los notebooks o corriendo el programa principal .py. Ambos son análogos y solo cambia su forma de ejecución propia del notebook/consola.

Para leer notebooks: El proyecto se dividió en cuatro notebooks donde cada una cumple una función, la elección de hacer tantos notebooks fue hecha con base al juicio de los integrantes en el mejor entendimiento para los lectores: El primer notebook es llamado Extracción.ipynb que corre **únicamente** en Linux, y trae las herramientas usadas para el parseo de los horarios del semestre 2021-1. Ningún otro notebook requiere linux, debido a que este guarda el scrapping hecho en la carpeta ciencias_horarios para la próxima lectura de los demás programas. El segundo notebook es ParserMaterias, que análogo al primero, trae el parseo necesario pero para los planes de estudio de las optativas, para así crear un recomendador de materias optativo. El tercer notebook se titula Funciones.ipynb y es el de interés para entender el algoritmo detrás del proyecto, pues trae el algoritmo combinatorio explicado en la documentación ejecutiva. Finalmente, el notebook que junta los dos anteriores se titula Proyecto.ipynb y hace la ejecución de todos los notebooks además de incluír el programa principal e interfaz de usuario, así como unas pruebas de tiempos de ejecución.

Así mismo, se incluye un único programa Proyecto.py que junta los tres últimos notebooks en un archivo de python y puede ejecutarse desde terminal.

Finalmente las demás carpetas son las bases de datos que fueron obtenidas mediante los programas. De esta manera pasamos de bases de datos no estructuradas a estructuradas.

Link edit Overleaf [aqui](https://www.overleaf.com/1117179873rrwhnmvvqjqh)
