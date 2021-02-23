from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from numpy import linspace
import pandas as pd

import json
import random
import warnings
import itertools
import os
import time
import unidecode #pip install unidecode



directory = "data/planes_materias/TXT/"

materias = {}
#print("hola")
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        #print(filename)
        f = open(os.path.join(directory, filename), 'r')
        materias[filename[:-4]] = f.read()

#print(materias['1.txt'])


# In[90]:


stop_words = ['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le',
'ya', 'o', 'este', 'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos',
'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa',
'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas',
'nosotras', 'vosotros', 'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 
'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 
'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos', 'estabais', 
'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 
'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis', 'han', 'haya', 
'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían', 'había', 'habías', 
'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 
'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis', 
'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería', 'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 
'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos',
'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos',
'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía', 'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis',
'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 
'tenidas', 'tened', 'CARRERA', 'MATEMATICO', 'SERIACION', 'INDICATIVA', 'ANTECEDENTE', 'MODALIDAD', 'CURSO', 'CARACTER', 'TEORICAS', 'PRACTICAS', 'CREDITOS', 'HORAS', 'SEMANA', 'SEMESTRE', 
'CLAVE', 'FACULTAD', 'CIENCIAS', 'OBJETIVO', 'BIBLIOGRAFIA', 'BASICA', 'COMPLEMENTARIA', 'SUGERENCIA', 'PARA', 'LA', 'EVALUACION', 'DE', 'LA', 'ASIGNATURA', 'Ademas', 'de', 'las',
 'calificaciones', 'en', 'examenes', 'y', 'tareas', 'se', 'tomara', 'en', 'cuenta', 'la', 'participacion', 'del', 'alumno', 'PERFIL', 'PROFESIOGRAFICO', 'Matematico', 'fisico', 'actuario', 
 'o', 'licenciado', 'en', 'ciencias', 'de', 'la', 'computacion', 'especialista', 'en', 'el', 'area', 'de', 'la', 'asignatura', 'a', 'juicio', 'del', 'comite', 'de', 'asignacion', 'de', 
 'cursos', 'UNIDADES', 'TEMATICAS', 'SERIACION', 'INDICATIVA', 'ANTECEDENTE', 'SUBSECUENTE', 'optativo', 'Optativas']


TfidfVectorizer(stop_words=stop_words)


# In[91]:



def train(intereses):
    
    materias[0] = intereses
    #data = pd.DataFrame(materias)
    data = pd.Series(materias).to_frame()
    type(data)
    data = data.rename(columns={0: 'Planes'})
    #data["index"] = pd.to_numeric(data["index"])
    data.index = data.index.map(int)
    data.sort_index(inplace=True)

    #print(data.columns)
    #print(data.index)


    #Define a TF-IDF Vectorizer Object. Remove all spanis stop words such as 'de', 'la', 'que', 'el'
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        tfidf = TfidfVectorizer(stop_words)

    #Construct the required TF-IDF matrix by fitting and transforming the data
    #print(data['Planes'])
    tfidf_matrix = tfidf.fit_transform(data['Planes'])

    #Output the shape of tfidf_matrix
    tfidf_matrix.shape

    #Palabras encontradas en todos los archivos
    tfidf.get_feature_names()[2990:3007]


    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    (cosine_sim.shape)
    #print(cosine_sim[1])

    return data, cosine_sim



# In[92]:


#indices = pd.Series(data.index, index=data.index).drop_duplicates()

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(intereses):
    # Get the index of the movie that matches the title
    data, matriz_similitudes = train(intereses)

    # Get the pairwsie similarity scores of all plans with la lista
    sim_scores = list(enumerate(matriz_similitudes[0]))
    #print(sim_scores)

    # Sort the topics based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #print(sim_scores)
    # Get the scores of the  10most similar topics
    sim_scores = sim_scores[0:11]
    scores = [i[1] for i in sim_scores]
    # Get the movie indices
    recomendaciones = [i[0] for i in sim_scores]
    #print(recomendaciones)

    # Return the top 10 most similar topics
    return list(data.iloc[recomendaciones].index[1:]),scores[1:]







with open('ciencias_horarios/materias_limpio20212.json') as archivo:
    materias_limpio = json.load(archivo)

with open('ciencias_horarios/semestres/1.json') as archivo:
    primer_sem = json.load(archivo)
with open('ciencias_horarios/semestres/2.json') as archivo:
    segundo_sem = json.load(archivo)
with open('ciencias_horarios/semestres/3.json') as archivo:
    tercer_sem = json.load(archivo)
with open('ciencias_horarios/semestres/4.json') as archivo:
    cuarto_sem = json.load(archivo)
with open('ciencias_horarios/semestres/5.json') as archivo:
    quinto_sem = json.load(archivo)
with open('ciencias_horarios/semestres/6.json') as archivo:
    sexto_sem = json.load(archivo)
with open('ciencias_horarios/semestres/op1.json') as archivo:
    optativas_1 = json.load(archivo)
with open('ciencias_horarios/semestres/op2.json') as archivo:
    optativas_2 = json.load(archivo)
with open('ciencias_horarios/semestres/op3.json') as archivo:
    optativas_3 = json.load(archivo)

class materia():
    '''
    Clase que contendrá la información de una materia
    '''
    def __init__(self, clave,materia):
        '''
        Función de inicialización que creará el diccionario con los
        grupos de la materia, y un diccionario cuyas llaves serán los días
        de la semana y a su vez cada una contendrá un diccionario con las
        horas y los grupos que imparten la materia en cada hora.
        -------------------------------------------------------------------
        :param clave str: Cadena de cuatro dígitos que contiene la clave
                         de la materia
        :param materia str: Cadena con el nombre de la materia
        '''
        self.grupos = {}
        self.clave = clave
        self.nombre = materia
        self.horarios = {
            'lu':{},
            'ma':{},
            'mi':{},
            'ju':{},
            'vi':{},
            'sa':{}
        }

    def agregar_grupo(self,grupo,profesor,horario):
        '''
        Función de agregació  de grupos a la clase. Agregará
        el grupo al diccionario `grupos` así como actualización
        del diccionario de horarios.
        -----------------------------------------
        :param grupo str: Cadena de 4 dígitos con el número de grupo.
        :param profesor str: Nombre del docente del grupo.
        :param horario dict: Diccionario que incluye el horario por día
        '''
        for dia in horario.keys():
            #print(horario[dia])
            if horario[dia] !=[]:
                hora_dia = tuple(horario[dia][0])

                if hora_dia not in list(self.horarios[dia].keys()):

                    self.horarios[dia][hora_dia] = []
                self.horarios[dia][hora_dia].append(grupo)

        self.grupos[grupo] = [profesor,horario]


# Y guardamos cada materia como un objeto de la clase:

# In[9]:


dict_materias = {}
claves = []
grupos_claves = {}
for materia_limpio in materias_limpio:
    clave = materia_limpio['clave']
    if clave not in claves:
        claves.append(clave)
        asignatura = materia_limpio['materia']
        mat = materia(clave,asignatura)
        dict_materias[clave] = mat

    grupo = materia_limpio['grupo']
    profesor = materia_limpio['profesor']
    horario = materia_limpio['horario']
    grupos_claves[grupo] = clave
    dict_materias[clave].agregar_grupo(grupo,profesor,horario)


# Algunas funciones para pasar de claves a nombres y grupos, así como otras funciones útiles

# In[10]:


def str_to_clave(clave):
    '''
    Función que convierte un entero a una clave
    en cadena de texto 4 dígitos
    '''
    clave_str = str(clave)
    clave_str = '0'*(4-len(clave_str))+clave_str
    return clave_str

def clave_to_nombre(clave):
    '''
    Dada una clave , regresa el nombre de la asignatura
    '''
    if isinstance(clave, int):
        clave_str = str_to_clave(clave)
        return dict_materias[clave_str].nombre

    return dict_materias[clave].nombre


def get_horario(clave,hora_inicio,dia):
    '''
    Dada una clave, regresa todos los grupos que comiencen a
    la hora dada.

    :param clave str: Cadena de 4 dígitos que indica la materia
    :param hora_inicio float: Hora a la que inicia la clase
    :para dia str: Cadena de dos letras que indica el día del horario.

    :returns False: En caso de que no haya algún grupo en ese horario
    :returns (horario_inicio,horario_fin), grupos:
                    Regresa una tupla con inicio y fin de la materio junto
                    a sus grupos.
    '''
    materia = dict_materias[clave]
    for horario in materia.horarios[dia].keys():
        if hora_inicio == horario[0]:
            return horario, materia.horarios[dia][horario]
    return False

def grupo_to_clave(grupo):
    '''
    Regresa a qué materia pertenece un grupo específico
    -----------------------------------------------------
    :param grupo str: Cadena de 4 dígitos de un grupo

    :returns str: Cadena de 4 dígitos que representa la materia
    '''
    return grupos_claves[grupo]


# La siguiente función nos permite obtener toda la información de una materia con solo el código de grupo

# In[17]:



def grupo_info(grupo):
    '''
    Da la información de un grupo
    --------------------------------------
    :param grupo str: Cadena de 4 dígitos de un grupo

    :returns: Profesor, Horario de la materia
    '''
    clave = grupo_to_clave(grupo)
    grupo = dict_materias[clave].grupos[grupo]
    profesor , horario = grupo
    horario = {dia:tuple(horario[dia][0]) for dia in horario.keys() if horario[dia] !=[]}
    return clave, profesor, horario

grupo_info('4117')


# ## Recomendador de horarios

# La siguiente función crea candidatos entre la hora de inicio y fin de un día:

# In[12]:


def generar_candidatos(claves,hora_inicio,hora_fin,dia):
    '''
    Para las claves e información sobre hora y día, regresa un diccionario con
    los grupos disponibles para esas materias en esas restricciones, es decir
    un diccionario cuyas llaves son intervalos de horas y sus valores los grupos
    que tienen clase a esa hora en ese día, eligiendo intervalos de horas entre
    la hora de inicio y fin establecidas.
    -------------------------------------------------
    :param claves [str]: Lista con las claves de materias a recuperar
    :hora_inicio float: Hora a la que inicia el horario debe ser entero o
                        un entero y medio (e.g 9.0 y 9.50 son válidos, mientras que
                        6:35 no es una hora válida) el 0.5 representa la media
                        hora.
    :hora_fin float: Hora máxima a la que termina el horario

    :returns horario_dia dict: Diccionario que tiene como llaves las horas que tienen candidatos,
                                con los candidatos a dicha hora
    :returns horas_disponibles list: Lista con los intervalos de horas que se consideran para los
                                candidatos, es decir cada grupo candidato imparte su clase en alguna
                                hora de esta lista.
    :returns grupos_por_clave dict: Diccionario que tiene como llaves las claves de las materias y
                                como valores, los grupos candidatos que se encontraron para cada
                                materia
    '''
    if hora_inicio%0.5 != 0 or hora_fin%0.5 != 0:
        raise Exception('Ese no es un horario válido, tiene que representar una hora o \n fracción de media hora')



    horario_dia = {}
    horas_disponibles = set()
    grupos_por_clave = {}
    #Un intervalo de las horas representadas en fracciones de media hora
    horas_eleccion =  linspace(hora_inicio,hora_fin,int(2*(hora_fin-hora_inicio)+1))

    #for dia in dias.keys():
    for clave in claves:
        grupos_por_clave[clave] = []
        for hora in horas_eleccion:
            horario = get_horario(clave,hora,dia)

            if horario is False: #si no hay grupos disponibles a esa hora
                continue
            if horario[0][1]>hora_fin: #Si el horario se pasa de la hora establecida
                continue

            hora_de_clase = horario[0]
            grupos = horario[1]
            if hora_de_clase not in horario_dia.keys():
                horario_dia[hora_de_clase] = []

            horas_disponibles.add(hora_de_clase)
            horario_dia[hora_de_clase] += grupos
            grupos_por_clave[clave] += grupos

    return horario_dia,list(horas_disponibles), grupos_por_clave

candidatos = generar_candidatos(['0002','0003','0083','0163','0715'],8.0,12,'lu')
candidatos


# Y a continuación la función para recomendar candidatos no solo para un día, sino para toda la semana:

# In[20]:


def generar_candidatos_semana(claves, hora_inicio, hora_fin):
    '''
    Función que da información acerca de los grupos que imparten clase
    entre dos horas establecidas.
    ---------------------------------------------------------------
    :param claves [str]: Lista con las claves de las materias a acomodar
    :param hora_inicio float: Hora a la que inicia el horario debe ser entero o
                        un entero y medio (e.g 9.0 y 9.50 son válidos, mientras que
                        6:35 no es una hora válida) el 0.5 representa la media
                        hora.
    :param hora_fin float: Hora máxima a la que termina el horario


    :returns horario_por_dia dict: Diccionario que tiene como llaves los días que tienen candidatos,
                                con los candidatos por intervalo de hora
    :returns horas_disponibles dict: Diccionario con los días e intervalos de horas que se consideran para los
                                candidatos, es decir cada grupo candidato imparte su clase en alguna
                                hora de este diccionario.
    :returns grupos_por_clave dict: Diccionario que tiene como llaves las claves de las materias y
                                como valores, los grupos candidatos que se encontraron para cada
                                materia
    '''
    dias = ['lu','ma','mi','ju','vi','sa']

    horario_por_dia = {}
    horas_disponibles_por_dia = {}
    grupos_por_clave = {}
    for dia in dias:
        candidatos_dia = generar_candidatos(claves,hora_inicio,hora_fin,dia)
        horario_por_dia[dia] = candidatos_dia[0]
        horas_disponibles_por_dia[dia] = candidatos_dia[1]
        for intervalo in candidatos_dia[2].keys():
            if intervalo not in grupos_por_clave.keys():
                grupos_por_clave[intervalo] = []
            grupos_por_clave[intervalo]+= candidatos_dia[2][intervalo]
    grupos_por_clave = {intervalo:list(set(grupos_por_clave[intervalo]))
                       for intervalo in grupos_por_clave.keys()}
    return horario_por_dia, horas_disponibles_por_dia, grupos_por_clave

candidatos = generar_candidatos_semana(['0002','0001','0715'],8.0,11)
candidatos


# A continuación se definen funciones para acomodar horarios en las que se verifica si un intervalo de tiempo interfiere con un horario establecido para un día, después lo mismo pero intervalos de tiempo en una semana, y finalmente una función que compara los horarios a las que se imparten materias una lista de grupos y verifica si alguna se intersecta con algún otro grupo

# In[22]:


def se_intersecta(intervalo,horario_dia):
    '''
    Dado un intervalo de tiempo y un horario, checa si alguna
    clase del horario se intersecta con el intervalo.

    :param intervalo tuple: Intervalo de tiempo a verificar
    :param hoarario dict: Diccionario que tiene como llaves días de la semana
                        y horas a las que se imparten materias desglosadas por
                        hora. Ejem:
            {'lu': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'ma': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'mi': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'ju': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'vi': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'sa': {}}

    :returns Bool: Verdadero si se intersectan, falso en otro caso.
    '''
    horario_lista = sorted(list(horario_dia.keys()),key= lambda x:x[1])
    inicio = intervalo[0]
    fin = intervalo[1]
    for hora in horario_lista:
        hora_inicio = hora[0]
        hora_fin = hora[1]
        if hora_inicio <= inicio < hora_fin or hora_inicio < fin <= hora_fin:
            return True
    return False

def se_intersecta_semana(intervalos,horario):
    '''
    Dado un horario de materia por día y un horario, checa si alguna
    clase del horario se intersecta con la materia.
    -----------------------------------------------------------------
    :param intervalo tuple: Horario de un grupo a verificar.
                               Ejem: {'lu': (10.0, 11.0),
                                      'ma': (10.0, 11.0),
                                      'mi': (10.0, 11.0),
                                      'ju': (10.0, 11.0),
                                      'vi': (10.0, 11.0)}
    :param hoarario dict: Diccionario que tiene como llaves días de la semana
                        y horas a las que se imparten materias desglosadas por
                        hora. Ejem:
            {'lu': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'ma': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'mi': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'ju': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'vi': {(10.0, 11.0): ['4212', '4213'], (9.0, 10.0): ['4175', '4176']},
              'sa': {}}

    :returns Bool: Verdadero si se intersectan, falso en otro caso.
    '''
    dias = ['lu','ma','mi','ju','vi','sa']
    for dia in horario.keys():
        if dia in intervalos.keys():
            horario_dia = horario[dia]
            if se_intersecta(intervalos[dia],horario_dia):
                return True
    return False

prueba_dias = candidatos[0]
horario_prueba = grupo_info('4174')[2]
se_intersecta_semana(horario_prueba,prueba_dias)


# In[23]:


def conjunto_se_intersecta(grupos):
    '''
    Dado un conjunto de grupos, comprueba si los horarios
    de los grupos se intersectan
    -------------------------------------------------
    :param grupos [str]: Lista de grupos

    :return Bool: Indicador de si los conjuntos se intersectan o no.
    :returns Horario: Horario desglosado por día y hora
    '''
    dias = ['lu','ma','mi','ju','vi','sa']
    primer_horario = grupo_info(grupos[0])[2]
    horario = {dia:{} for dia in dias}

    for dia, hora in primer_horario.items():
        horario[dia][hora] = grupos[0]

    for grupo in grupos[1:]:
        horario_materia = grupo_info(grupo)[2]
        if se_intersecta_semana(horario_materia,horario):
            return True, horario
        for dia, hora in horario_materia.items():
            horario[dia][hora] = grupo

    return False, horario






def get_recomendations_str(intereses):
    '''
    Dado una cadena con los intereses de alguna persona, regresa el nombre
    de las materias que le recomienda.
    ----------------------------------------------------------
    :param intereses str: Cadena que tiene intereses del alumno
    :returns [str]: Lista con materias a considerar
    '''
    recomendaciones = []
    recomendaciones_num, scores = get_recommendations(intereses.lower())
    for recomendacion in recomendaciones_num:
        try:
            recomendaciones.append((clave_to_nombre(recomendacion),str_to_clave(recomendacion)))
        except Exception as e:
            pass
    return recomendaciones, scores



def conjunto_se_intersecta(grupos):
    '''
    Dado un conjunto de grupos, comprueba si los horarios
    de los grupos se intersectan
    -------------------------------------------------
    :param grupos [str]: Lista de grupos

    :return Bool: Indicador de si los conjuntos se intersectan o no.
    '''
    dias = ['lu','ma','mi','ju','vi','sa']
    primer_horario = grupo_info(grupos[0])[2]
    horario = {dia:{} for dia in dias}

    for dia, hora in primer_horario.items():
        horario[dia][hora] = grupos[0]

    for grupo in grupos[1:]:
        horario_materia = grupo_info(grupo)[2]
        if se_intersecta_semana(horario_materia,horario):
            return True, horario
        for dia, hora in horario_materia.items():
            horario[dia][hora] = grupo

    return False, horario
conjunto_se_intersecta(['4171','4172'])



def crear_horario(claves,hora_inicio,hora_fin,seed=None):
    '''
    Dada una lista de claves y hora de inicio y fin de un horario deseado,
    regresa un diccionario con el horario de esas materias, así como
    una lista de (clave,grupo) en caso de que sea posible formar el horario,
    en caso contrario, regresa Falso
    ----------------------------------------------------------------
    :param claves [str]: Lista de claves
    :param hora_inicio float: Hora de inicio de las clases representadas
                             en horas u horas y media (XX.0, XX.5)
    :param hora_fin float: Hora de fin de las clases representadas
                             en horas u horas y media (XX.0, XX.5)
    :param seed int: Semilla para la elección de grupos, en caso de no ser especificada,
                    la elección de grupos será aleatoria

    :returns False: En caso de no haber una combinación posible
    :returns horario dict: Diccionario con los días y las horas en que se tiene cada
                        materia. Ejem:
                        {'lu': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'ma': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'mi': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'ju': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'vi': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'sa': {}}
    :returns [(clave,grupo)]: Lista con las claves y grupos que se eligieron.
                            Ejem: [('0001', '4175'), ('0005', '4112')]
    '''
    if hora_inicio%0.5 != 0:
        raise Exception('Ese no es un horario válido, tiene que representar una hora o \n fracción de media hora')

    if seed is None:
        seed = random.randint(0,2**10)
    random.seed(seed)
    random.shuffle(claves)

    candidatos = generar_candidatos_semana(claves,hora_inicio,hora_fin)
    candidatos_por_clave = candidatos[2]
    for dia in candidatos_por_clave.keys():
        if candidatos_por_clave[dia] == []:
            return False #En caso de que no sea posible acomodar algún horario
        random.shuffle(candidatos_por_clave[dia])

    grupos = list(candidatos_por_clave.values())
    combinaciones = list(itertools.product(*grupos))
    for comb in combinaciones:
        if not conjunto_se_intersecta(comb)[0]:
            return conjunto_se_intersecta(comb)[1], list(zip(claves,comb))
    return False



def crear_horario_especial(claves,claves_personalizadas,hora_inicio,hora_fin,len_return=10,seed=None):
    '''
    Dada una lista de claves y hora de inicio y fin de un horario deseado,
    regresa un diccionario con el horario de esas materias, así como
    una lista de (clave,grupo) en caso de que sea posible formar el horario,
    en caso contrario, regresa Falso
    ----------------------------------------------------------------
    :param claves [str]: Lista de claves
    :param claves_personalizadas dict: Diccionario de aquellas claves personalizadas (se sabe 
                                    entre  que grupos se quiere meter).
                                    Ejem:{'0001':['4170','4171']} que significa que se desea cursar 
                                    la materia de álgebra moderna i ('0001') en alguno de los grupos
                                    '4170','4171'.
    :param hora_inicio float: Hora de inicio de las clases representadas
                             en horas u horas y media (XX.0, XX.5)
    :param hora_fin float: Hora de fin de las clases representadas
                             en horas u horas y media (XX.0, XX.5)
    :param len_return int: Número de opciones a devolver.
    :param seed int: Semilla para la elección de grupos, en caso de no ser especificada,
                    la elección de grupos será aleatoria

    :returns False: En caso de no haber una combinación posible
    :returns horario dict: Diccionario con los días y las horas en que se tiene cada
                        materia. Ejem:
                        {'lu': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'ma': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'mi': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'ju': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'vi': {(9.0, 10.0): '4175', (8.0, 9.0): '4112'},
                          'sa': {}}
    :returns [[(clave,grupo)]]: Lista con las claves y grupos que se eligieron.
                            Ejem: [('0001', '4175'), ('0005', '4112')]
    '''
    if hora_inicio%0.5 != 0:
        raise Exception('Ese no es un horario válido, tiene que representar una hora o \n fracción de media hora')

    if seed is None:
        seed = random.randint(0,2**10)
    random.seed(seed)
    random.shuffle(claves)

    candidatos = generar_candidatos_semana(claves,hora_inicio,hora_fin)
    candidatos_por_clave = candidatos[2]
    candidatos_por_clave.update(claves_personalizadas)
    for dia in candidatos_por_clave.keys():
        if candidatos_por_clave[dia] == []:
            return False #En caso de que no sea posible acomodar algún horario
        random.shuffle(candidatos_por_clave[dia])

    grupos = list(candidatos_por_clave.values())
    combinaciones = list(itertools.product(*grupos))
    posibles_horarios = []
    claves_comb = claves+list(claves_personalizadas.keys())
    for comb in combinaciones:
        if not conjunto_se_intersecta(comb)[0]:
            posibles_horarios.append([conjunto_se_intersecta(comb)[1], list(zip(claves_comb,comb))])
            if len(posibles_horarios)==len_return:
                break
    if posibles_horarios != []:
        return posibles_horarios
    return False



with open('ciencias_horarios/semestres/1.json') as archivo:
    primer_sem = json.load(archivo)
with open('ciencias_horarios/semestres/2.json') as archivo:
    segundo_sem = json.load(archivo)
with open('ciencias_horarios/semestres/3.json') as archivo:
    tercer_sem = json.load(archivo)
with open('ciencias_horarios/semestres/4.json') as archivo:
    cuarto_sem = json.load(archivo)
with open('ciencias_horarios/semestres/5.json') as archivo:
    quinto_sem = json.load(archivo)
with open('ciencias_horarios/semestres/6.json') as archivo:
    sexto_sem = json.load(archivo)
with open('ciencias_horarios/semestres/op1.json') as archivo:
    optativas_1 = json.load(archivo)
with open('ciencias_horarios/semestres/op2.json') as archivo:
    optativas_2 = json.load(archivo)
with open('ciencias_horarios/semestres/op3.json') as archivo:
    optativas_3 = json.load(archivo)

"""
ESTO ES PARA VER COMO DEBEN IR LOS NODOS EN LATEX. EN CASO DE PASAR A LATEX
\node[a1] at (1,16) {VisualInfo};
\node[a1] at (4,16) {VisualInfo};
\node[a1] at (5,16) {VisualInfo};
\node[a1] at (4,17) {VisualInfo};
\node[a1] at (5,17) {VisualInfo};
"""



def horario_toStr(horario):
    latex = ""
    if horario == False:
        #print("Lo siento, no fue posible crear un horario con estas materias")
        print('*'*30)
    else:
        #print("Creamos el siguiente horario con los siguientes grupos:\n")
        for materia in horario[1]:
            print("~~."*12,'\n',
                  f"{clave_to_nombre(materia[0]).capitalize()}\n",
                  f"Grupo {materia[1]}",
                  f"Profesor(a):{grupo_info(materia[1])[1].title()}")

        print("\n .-.-.-.-.-.-.-.-.-.-. \n")
        for dia in horario[0]:
            print("\n")
            for clase in horario[0][dia]:

                aux = horario[0][dia][clase]
                clave_materia, profesor, horas = grupo_info(aux)
                if dia == 'lu':
                    print("Lunes ->",clase,"->",clave_to_nombre(clave_materia))
                if dia == 'ma':
                    print("Martes ->",clase,"->",clave_to_nombre(clave_materia))
                if dia == 'mi':
                    print("Miercoles ->",clase,"->",clave_to_nombre(clave_materia))
                if dia == 'ju':
                    print("Jueves ->",clase,"->",clave_to_nombre(clave_materia))
                if dia == 'vi':
                    print("Viernes ->",clase,"->",clave_to_nombre(clave_materia))
                if dia == 'sa':
                    print("Sabado ->",clase,"->",clave_to_nombre(clave_materia))





def main(inicio,fin):
    print("Hola este es el súper creador de horarios 9000! \n")

    materias_eleccion ={
        '1':primer_sem,
        '2':segundo_sem,
        '3':tercer_sem,
        '4':cuarto_sem,
        '5':quinto_sem,
        '6':sexto_sem,
        '7':'7',
        '8':'8',
    }
    lista_deseados = []

    while(True):
        if len(lista_deseados)>0:
            print('\nHasta ahora has seleccionado')
            for materia in lista_deseados:
                try:
                    print(clave_to_nombre(materia))
                except Exception:
                    print(f'Lo sentimos, no se puede armar el horario, pues la optativa {materia} no \n se abrió este semestre.')
                    raise
            print(f'Claves: {lista_deseados}')

        print('\n Elige materias de algún semestre:\n',
         """
         1 -> Primer Semestre
         2 -> Segundo Semestre
         3 -> Tercer Semestre
         4 -> Cuarto Semestre
         5 -> Quinto Semestre
         6 -> Sexto Semestre
         7 -> Optativas
         8 -> Recomendador de optativas
         """)

        eleccion = str(input('\n Eliga algún número: '))
        while(eleccion not in materias_eleccion.keys()):
            eleccion = str(input('Esa no es una opción válida, eliga una opción válida: '))

        if eleccion != "7" and eleccion != "8":
            materias_sem = list(enumerate(materias_eleccion[eleccion].items()))
            print(f'Las materias del {eleccion}° semestre son:')

            for num, materia in materias_sem:
                print(f'{num} -> {materia[1]}')

            print("\nPor favor usa los indices para elegir que deseas cursar: \n")
            #print("Elige las materias que desees tomar, separados por comas\n")
            elecciones = input("Elige las materias que desees tomar, separados por comas: ")
            print("\n .-.-.-.-.-.-.-.-.-.-. \n")
            elecciones = elecciones.split(",")

            for num in elecciones:
                lista_deseados.append(materias_sem[int(num)][1][0])

            continuar = str(input('¿Quiere seguir eligiendo materia? [S/N]')).lower()

            while continuar !='s' and continuar !='n':
                continuar = str(input('Eliga una opción válida [S/N]')).lower()
            if continuar =='n':
                break
            else:
                continue




        if eleccion == '7':
            optativas = [optativas_1, optativas_2, optativas_3]
            print('Seleccione el nivel de optativas:')
            print('''
            0 <- Niveles I, II, III, IV
            1 <- Niveles V,VI
            2 <- Niveles VII,VIII
            ''')
            opt_eleccion = str(input('Eliga el índice del nivel de optativas: '))
            while opt_eleccion not in ('0','1','2'):
                opt_eleccion = str(input('Seleccione un índice correcto: '))

            if opt_eleccion =='0':
                optativa = list(enumerate(optativas[0].items()))

                for num, materia in list(enumerate(optativas[0].items())):
                    print(f'{num} <- {materia[1]}')

                print("\nPor favor usa los indices para elegir que deseas cursar: \n")
                #print("Elige las materias que desees tomar, separados por comas\n")
                elecciones = input("Elige las materias que desees tomar, separados por comas: ")
                print("\n .-.-.-.-.-.-.-.-.-.-. \n")
                elecciones = elecciones.split(",")

                for num in elecciones:
                    lista_deseados.append(optativa[int(num)][1][0])

                continuar = str(input('¿Quiere seguir eligiendo materia? [S/N]')).lower()

                while continuar !='s' and continuar !='n':
                    continuar = str(input('Eliga una opción válida [S/N]')).lower()
                if continuar =='n':
                    break
                else:
                    continue


            if opt_eleccion =='1':
                optativa = list(enumerate(optativas[1].items()))
                for num, materia in list(enumerate(optativas[1].items())):
                    print(f'{num} <- {materia[1]}')

                print("\nPor favor usa los indices para elegir que deseas cursar: \n")
                print("Elige las materias que desees tomar, separados por comas\n")
                elecciones = input("Elige las materias que desees tomar, separados por comas: ")
                print("\n .-.-.-.-.-.-.-.-.-.-. \n")
                elecciones = elecciones.split(",")

                for num in elecciones:
                    lista_deseados.append(optativa[int(num)][1][0])

                continuar = str(input('¿Quiere seguir eligiendo materia? [S/N]')).lower()

                while continuar !='s' and continuar !='n':
                    continuar = str(input('Eliga una opción válida [S/N]')).lower()
                if continuar =='n':
                    break
                else:
                    continue


            if opt_eleccion =='2':
                optativa = list(enumerate(optativas[2].items()))
                for num, materia in list(enumerate(optativas[2].items())):
                    print(f'{num} <- {materia[1]}')

                print("\nPor favor usa los indices para elegir que deseas cursar: \n")
                print("Elige las materias que desees tomar, separados por comas\n")
                elecciones = input("Elige las materias que desees tomar, separados por comas: ")
                print("\n .-.-.-.-.-.-.-.-.-.-. \n")
                elecciones = elecciones.split(",")

                for num in elecciones:
                    lista_deseados.append(optativa[int(num)][1][0])

                continuar = str(input('¿Quiere seguir eligiendo materia? [S/N]')).lower()

                while continuar !='s' and continuar !='n':
                    continuar = str(input('Eliga una opción válida [S/N]')).lower()
                if continuar =='n':
                    break
                else:
                    continue


        if eleccion =='8':

            interes = str(input('Escibe algunos intereses que tengas: '))
            print("Buscaremos horarios para estos intereses: \n" + interes)
            recomendaciones = get_recomendations_str(interes)

            print("\n .-.-.-.-.-.-.-.-.-.-. \n")
            print("El algoritmo suguiere las siguientes materias para ti: \n")
            claves_materias = []
            i = 0
            for recomendacion in recomendaciones:
                print(i,"->",recomendacion[0])
                claves_materias.append(recomendacion[1])
                i += 1

            print("\nPor favor usa los indices para elegir que deseas cursar: \n")
            
            elecciones = input("Elige las materias que desees tomar, separados por comas: ")
            print("\n .-.-.-.-.-.-.-.-.-.-. \n")


            elecciones = elecciones.split(",")
            for num in elecciones:
                lista_deseados.append(claves_materias[int(num)])
                print("Elegiste las siguientes opciones:",num)

            continuar = str(input('¿Quiere seguir eligiendo materia? [S/N]')).lower()

            while continuar !='s' and continuar !='n':
                continuar = str(input('Eliga una opción válida [S/N]')).lower()
            if continuar =='n':
                break
            else:
                continue



    if len(lista_deseados)>0:
        print('\nHasta ahora has seleccionado')
        for materia in lista_deseados:
            try:
                print(clave_to_nombre(materia))
            except Exception:
                print(f'Lo sentimos, no se puede armar el horario, pues la optativa {materia} no \n se abrió este semestre.')
                raise
        print(f'Claves: {lista_deseados}')

    print("\n .-.-.-.-.-.-.-.-.-.-. \n")
    print("Crearemos un horario en el que entres a las:",inicio,"y salgas a las:",fin," \n")
    horario = crear_horario(lista_deseados,inicio,fin)
    horario_toStr(horario)



if __name__ == '__main__':
    #inicio = int(input('Seleccione una hora de entrada: '))
    #fin = int(input('Seleccione una hora de salida: '))
    #main(inicio,fin)
    print(crear_horario_especial(['0766'],{'0001':['4170']},8,13))
    print(stop_words)
    