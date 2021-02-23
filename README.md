# Creador de Horario Facultad de Ciencias UNAM
En este repositorio se encuentran los programas necesarios, así como la interfaz gráfica de la herramienta que apoya a construir horarios del semestre 2021-2 a los estudiantes de la Facultad de Ciencias de la UNAM.

## Requisitos:

Python 3.8+ (https://www.python.org/downloads/)

Pandas (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

`pip install pandas`

Scikit-Learn (https://scikit-learn.org/stable/install.html)

`pip install -U scikit-learn`

Unidecode 

`pip install unidecode`

Tkinter (en caso de no venir instalado en la versión de python) https://tkdocs.com/tutorial/install.html

## Uso:
 Para hacer uso del recomendador, solo es necesario la ejecución de `main.py`. Una vez ejecutado el programa, se verá una ventana como esta:
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen1.png?raw=true)

En principio podemos elegir entre tres botones: Seleccionador de Materias, Recomendador de Optativas y Creación de Horarios.

### Seleccionador de materias

Al presionar el botón de Seleccionar Materias, se desplegaran los distintos semestres de materias, aśi como los bloques de materias optativas que se abrieron durante el semestre:

![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen2.png?raw=true)
 
Enseguida, al hacer la selección de alguna opción, se desplegarán las materias de ese semestre:
 
![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen3.png?raw=true)

Hacer click sobre algún nombre de materia, agregará la materia a la lista de materias seleccionadas, volver a hacer click en la materia, la quitará de la selección.

![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen4.png?raw=true)
 
 Al seleccionar la pestaña de *Grupos*, mostrará en otra ventana aquellos grupos de la amteria seleccionada.
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen5.png?raw=true)
 
 Y al seleccionar en esta ventana, algún grupo, lo agregará a la lista de materias agregadas, pero se notará que aparecerá la materia con un paréntesis, eso significa que únicamente se están considerando los grupos que están adentro del paréntesis. Esto es, al hacer el horario, se seleccionará alguno de los grupos que están adentro de los paréntesis para cada materia.
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen6.png?raw=true)
 
 En el siguiente ejemplo, al considerar la elección para la materia de cálculo, se eligirá alguno de los grupos 4015,4016,4017. Si se selecciona *Quitar Grupo* quitará la elección del grupo.
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen7.png?raw=true)
 
 ### Crear Horario
 
 Una vez seleccionadas las materias deseadas, podemos presionar el botón de creación de horario, donde ahora aparecerá una pantalla como la siguiente:
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen8.png?raw=true)
 
 En la pantalla, con ayuda de las cajas de selección de horas, se elige una hora de entrada (6:00) y una hora de salida (14:00). Esto indica que se desea un horario que empiece a las seis de la mañana y termine a las dos de la tarde (el algoritmo podrá elegir combinaciones de materias que estén entre las seis y dos de la tarde). Para fijar el horario, es necesario apretar el botón *Registrar* Y se mostrará la eetiqueta que indica que el horario se ha resgistrado correctamente.
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen9.png?raw=true)
 
 Una vez realizado esto, para dar las recomendaciones de horario, se presionará el botón *Crear Horario* que está en amarillo. Y enseguida se mostrarán hasta 10 opciones de horarios distintos en la terminal:
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen11.png?raw=true)
 
 En caso de que no exista alguna combinación posible de horario con las elecciones hechas, se mostrará un mensaje de no compatibilidad.
 
 ### Recomendador de optativas.
 
 Para apoyar en la tarea de orientar la elección de materias optativas, existe la opción de recomendación de optativas, y al presionarlo se muestra la siguiente pantalla:
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen12.png?raw=true)
 
 En ella se encuentra una caja de texto (con algunas recomendaciones por default) en donde los alumnos podrán escribir sus intereses y mediante el método `TfidfVectorizer` de scikit-learn, recomendará materias optativas en función a la aparición de los términos escritos en los distintos planes de estudio para cada materia. Una vez elegidos nuestro intereses, podremos presionar el botón de recomendación para que se muestren hasta 10 materias recomendadas:
 
 ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen13.png?raw=true)

Existen cuatro columnas en estas recomendaciones:
- Afinidad: Es un indicador de similitud de las materias con los intereses. No está establecido una afinidad máxima, pero se puede considerar que una materia tiene buena afinidad con los intereses si se encuentra cerca de una afinidad de 30 puntos, mientras que se puede cosniderar que una afinidad de menos de 10 puntos, indica que existen algunos intereses en el contenido de la materia, pero no es tanto el contenido.
- Materia: Nombre de la materia.
- Información: Estos botones nos mostrarán los planes de estudio de cada materia que se abrirá en el navegador web predeterminado:
   ![alt text](https://github.com/Gcota51/Horario-Scheduler/blob/master/data/Imagenes/Imagen14.png?raw=true)
- Agregar: Agregará la materia a la lista de naterias para armar el horario.


Proyecto elaborado por Guillermo Cota Martínez (https://github.com/Gcota51) en colabroación con Jorge Macías Gómez (https://github.com/UlmoMacias) para la materia de *Matemáticas Discretas* de la Licenciatura en Ciencia de Datos de la UNAM impartida por el Dr. Leonardo Ignacio Martínez Sandoval (https://www.nekomath.com/)
