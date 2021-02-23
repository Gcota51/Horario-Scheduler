import tkinter as tk
import time
from Funciones import *
from tkinter import Button, Label, Frame, Entry
from tkinter import font as tkFont
import webbrowser


top = tk.Tk()
top.title('Programa Horarios')

frames = ['','']

materias_seleccionadas = []
materias_seleccionadas_por_grupo = {}

texto = Label(top, text='Bienvenido al creador de horarios, seleccione una opción.')
texto.grid(row=0,columnspan=3)

texto_abajo = Label(top,text='')
texto_abajo.grid(row=2,columnspan=3)

cuadro = []
eleccion_materias = []
eleccion_materias_por_grupo = {}
intervalo = []

bottom = Frame(top, bg='white')
bottom.grid(columnspan=3)
cuadro.append(bottom)

#Fonts
helv10 = tkFont.Font(family='Helvetica', size=10)
helv8 = tkFont.Font(family='Helvetica', size=8)
helv7 = tkFont.Font(family='Helvetica', size=7)




def texto():
    """Función que actualizará el texto de las materias seleccionadas

    Returns:
        str: String de las materias
    """
    texto_1 = ', '.join(clave_to_nombre(clave).capitalize() 
                                    for clave in  eleccion_materias)
    if eleccion_materias_por_grupo == {}:
        return f'Materias Seleccionadas:\n{texto_1}'
    texto_2 = ''
    for clave, grupos in eleccion_materias_por_grupo.items():
        materia = clave_to_nombre(clave)
        texto_2 += f'{materia.title()} ({", ".join(grupos)})'
    return f"Materias Seleccionadas:\n{texto_1},\n{texto_2}"

def mostrar_info(clave):
    """Función que mostrará información sobre alguna materia: Grupos y profesores.

    Args:
        clave (int): Clave de materia
    """
    if clave in eleccion_materias:
        eleccion_materias.remove(clave)
    else:
        eleccion_materias.append(clave)
    
    texto_abajo.config(text=texto())

def semestres():
    """
    Función que mostrará los semestres
    """


    def agregar_grupo(grupo, botones_por_materia,botones):
        """Función que agregará un grupo en las materias candidatas

        Args:
            grupo (str): Grupo a eleccion
            botones_por_materia (dict): Diccionario con los botones de la selección de materias
            boton (tk.Button): Botón que invoca la función
        """
        clave_grupo = grupo_to_clave(grupo)
        boton = botones[grupo]
        if clave_grupo in eleccion_materias_por_grupo.keys(): 
            if grupo in eleccion_materias_por_grupo[clave_grupo]: #Quitar
                eleccion_materias_por_grupo[clave_grupo].remove(grupo)
                boton.config(bg = 'blue', text='Agregar Grupo')
                if eleccion_materias_por_grupo[clave_grupo] == []:
                    del eleccion_materias_por_grupo[clave_grupo]
            else:
                eleccion_materias_por_grupo[clave_grupo].append(grupo)
                boton.config(bg = 'orange', text='Quitar Grupo')
        
        else:
            eleccion_materias_por_grupo[clave_grupo] = [grupo]
            boton.config(bg = 'orange', text='Quitar Grupo')
        
        if clave_grupo in botones_por_materia.keys():
            botones_por_materia[clave_grupo].config(state=estado(clave_grupo))
        
        texto_abajo.config(text=texto())


    def estado(clave):
        """Función de estado de un botón para una clave, si hay alguna materia que ya se haya
        'personalizado', es decir si se eligió algún grupo(s) específico de la materia.

        Args:
            clave (int): Clave de la materia
        
        Returns:
            tk.DISABLED: Si la materia ya fue 'personalizada'
            tk.ACTIVE : En otro caso
        """ 
        if clave in eleccion_materias_por_grupo.keys():
            return tk.DISABLED
        return tk.ACTIVE




    def grupos_clave(clave,botones_por_materia):
        """Función que mostrará los grupos disponibles para una materia

        Args:
            clave (int): Clave de la materia
            botones_por_materia (dict): Diccionario con los botones de la selección de materias
        """
        grupo_window = tk.Tk()
        grupo_window.title(f'{clave_to_nombre(clave)}'.capitalize())
        i = 1
        
        label1 = Label(grupo_window, text='Grupo')
        label2 = Label(grupo_window, text='Profesor(a)')
        label3 = Label(grupo_window, text='Horario')
        
        label1.grid(row=0,column=0)
        label2.grid(row=0,column=1)
        label3.grid(row=0,column=2)
        botones_grupo = {}
        for grupo in dict_materias[clave].grupos.keys():
            grupo_frame = Frame(grupo_window)
            clave, grupo_prof,grupo_hora = grupo_info(grupo)
            dias = grupo_hora.keys()
            horas = grupo_hora.values()
            horas = [str(hora)[1:-1].replace('.0',':00').replace('.5',':30').replace(',','-')
                    for hora in horas]
            grupo_hora = ', '.join([f'{dia}~{hora}' 
                                    for dia,hora in zip(dias,horas)])
            
            grupo_label = Label(grupo_window, font=helv10, text=grupo)
            profe_label = Label(grupo_window, font= helv7, text=f' {grupo_prof.title()} ')
            hora_label = Label(grupo_window, font= helv7, text=grupo_hora)                
            
            
            agregar_button = Button(grupo_window, text='Agregar Grupo',
                                    command= lambda param=[grupo,botones_grupo]: 
                                    agregar_grupo(param[0],botones_por_materia,param[1]),
                                    bg='blue')
            botones_grupo[grupo] = agregar_button
            grupo_label.grid(row = i, column=0)
            profe_label.grid(row = i, column=1)
            hora_label.grid(row = i, column=2)
            agregar_button.grid(row=i, column=3)
            
            i +=1


        grupo_window.mainloop()


    def seleccion_semestre(i):
        """Función que mostrará las materias de algún semestre

        Args:
            i (int): Número de semestre.1 para 0-5 y para los restantes, indica el número
                     de agrupamiento de materias optativas.
        """
        materias_eleccion = [primer_sem,segundo_sem,tercer_sem,cuarto_sem,
                             quinto_sem,sexto_sem,optativas_1, 
                             optativas_2, optativas_3]
        materias_sem = list(enumerate(materias_eleccion[i].items()))
        bottom = cuadro.pop()
        bottom.destroy()
        bottom = Frame(top, bg='white')
        bottom.grid(columnspan=3)
        cuadro.append(bottom)
        frames[1] = bottom

        i = 0
        j = 0
        
        botones_por_materia = {}

        for num, materia in materias_sem:
                clave = materia[0]
                if clave in dict_materias.keys():
                    materia_actual = 0
                    materia_nom = f'{materia[1]}'
                    materia_frame = Frame(bottom,bg='white')
                    button_materia = Button(materia_frame, text= materia_nom, font=helv7,
                                        command= lambda clave=clave: mostrar_info(clave),
                                         state=estado(clave))
                    button_informacion = Button(materia_frame,text='Grupos',font=helv7,bg='cyan',
                                                command = lambda clave=clave: grupos_clave(clave,botones_por_materia)) 
                    button_materia.config(width=50)
                    botones_por_materia[clave] = button_materia
                    button_materia.pack(side='left')
                    button_informacion.pack(side='left')
                    materia_frame.grid(row=i%20, column=j)
                    i+=1
                    if i%20==0:
                        j+=1
        
    try:
        frames[0].destroy()
    except Exception:
        pass
    frame_materias = Frame(top)  
    frames[0] = frame_materias
    primero   = Button(frame_materias,text='Primer Semestre',command = lambda: seleccion_semestre(0))
    segundo   = Button(frame_materias,text="Segundo Semestre",command = lambda: seleccion_semestre(1))
    tercero   = Button(frame_materias,text="Tercer Semestre",command = lambda: seleccion_semestre(2))
    cuarto    = Button(frame_materias,text="Cuarto Semestre",command = lambda: seleccion_semestre(3))
    quinto    = Button(frame_materias,text="Quinto Semestre",command = lambda: seleccion_semestre(4))
    sexto     = Button(frame_materias,text="Sexto Semestre",command = lambda: seleccion_semestre(5))
    optativa_1 = Button(frame_materias,text="Optativas niveles I-IV",command = lambda: seleccion_semestre(6))
    optativa_2 = Button(frame_materias,text="Optativas niveles V,VI",command = lambda: seleccion_semestre(7))
    optativa_3 = Button(frame_materias,text="Optativas niveles VII,VIII",command = lambda: seleccion_semestre(8))

    semestres_botones = [primero,segundo,tercero,cuarto,quinto,sexto,
    optativa_1,optativa_2,optativa_3]    


    column = 0
    row = 0
    
    for boton in semestres_botones:
        boton.config(font=helv10, height=1,width=25)
        boton.grid(column=column%3, row = row)
        if column%3==2:
            row += 1
        column += 1
    frame_materias.grid(row=3,columnspan=3)
    
        

def recomendador_optativas_window():

    frame_optativas = Frame(top)
    frame_optativas.grid(row=3,columnspan=3)
    try:
        frames[0].destroy()
        if frames[1] != '':
            frames[1].destroy()
    except Exception:
        pass
    frames[0] = frame_optativas

    texto_opt = Label(frame_optativas, text='Ingresa algunos intereses que tengas sin acentos')
    texto_opt.grid(columnspan=3)

    # https://stackoverflow.com/questions/30491721/how-to-insert-a-temporary-text-in-a-tkinter-entry-widget
    def on_entry_click(event):
        """function that gets called whenever entry is clicked"""
        if entry.get() == 'Enter your user name...':
            entry.delete(0, "end") # delete all the text in the entry
            entry.insert(0, '') #Insert blank for user input
            entry.config(fg = 'black')
        
    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, 'Enter your username...')
            entry.config(fg = 'blue')


    recomendaciones = ['Algebra abstracta', 'Topologia', 'Conjuntos', 'Teorema Limite Central', 'Procesos Poisson', 'Algoritmos','Sylow','Cohomologia','Isometria','Probabilidad','Teoria de Juegos','Inercia','Electromagnetismo','Renacimiento','Historia','Arboles Binarios','Conexidad','Conjuntos Abiertos','Epidemiologia']
    entry = Entry(frame_optativas, bd=1, width=60)
    entry.insert(0, ' '.join(random.sample(recomendaciones,3)))
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
    entry.grid(row=1,columnspan=3)

    eleccion_button = Button(frame_optativas,text='Recomendar Materias',
    command=lambda :recomendar(),bg='yellow')
    eleccion_button.grid(row=2,columnspan=3)
    
    af_text = Label(frame_optativas,text='Afinidad')
    af_text.grid(row=3,column=0)

    mat_text = Label(frame_optativas,text='Materia')
    mat_text.grid(row=3,column=1)
 
    def informacion(clave):
        """Función que abre el pdf de una materia por su clave

        Args:
            clave (int): Clave de la materia
        """
        path = f'data/planes_materias/pdf/{str(int(clave))}.pdf'
        webbrowser.open(path)

    def recomendar():
        """Función que asigna las recomendaciones

        Args:
            intereses ([type]): [description]
        """
        intereses = entry.get()
        recomendaciones, scores = get_recomendations_str(intereses)
        recomendaciones_buttons = []
        row = 4

        for recomendacion,score in zip(recomendaciones,scores):
            if score>0.01 and recomendacion[1] in dict_materias.keys():

                afinidad = score*200
                afinidad_label = Label(frame_optativas,text=f'{afinidad:.2f}')
                afinidad_label.grid(row=row,column=0)
                
                recomendacion_label = Label(frame_optativas,text=recomendacion[0])
                recomendacion_label.grid(row=row,column=1)
                
                recomendacion_button = Button(frame_optativas,text='Información',
                command=lambda clave=recomendacion[1]: informacion(clave),
                bg='blue')
                recomendacion_button.grid(row=row,column=2)
                
                agregar_button = Button(frame_optativas,text='Agregar',
                command=lambda clave=recomendacion[1]: mostrar_info(clave))
                agregar_button.grid(row=row,column=3)

                recomendaciones_buttons.append(recomendacion_button)
                row +=1


def crear_horario_window():
    """Función que contiene lo necesario para la ventana en donde se creará el horario.
    """
    
    def registrar_hora(etapa,inicio,fin,warning_label):
        """Función que registra la hora de inicio y fin

        Args:
            etapa (str): Si es 'inicio' entonces registra la hora de inicio y si es 'fin'
                        la de fin
            inicio (App): Reloj de inicio
            fin (App): Reloj de fin
            intervalo ([int]): Lista donde se guardan los intervalos de inicio y fin
            warning_label (Label): Etiqueta que avisará si el horario es correcto o no.
        """
        global intervalo
        inicio.trace_var()
        fin.trace_var()
        hora_inicio = int(inicio.last_value)
        hora_fin = int(fin.last_value)
        if hora_inicio>=hora_fin:
            warning_label.config(text='La hora de inicio tiene que ser antes que la de fin')
        else:
            intervalo = [hora_inicio,hora_fin]
            warning_label.config(text='Horario Registrado!')


    def hacer_horario(warning_label):
        """Función que genera un horario una vez que se tenga la información
        suficiente (grupos y horario de entrada/salida)


        Args:
            warning_label (Label): Etiqueta donde se pondrán los avisos
        """
        if intervalo==[]:
            warning_label.config(text='Seleccione hora de entrada y salida')
            return
        else:
            inicio = intervalo[0]
            fin = intervalo[1]
            if inicio >= fin:
                warning_label.config(text='Hora no válida')
            elif eleccion_materias==[] and eleccion_materias_por_grupo=={}:
                warning_label.config(text='No hay grupos seleccionados')
            else:
                opciones = crear_horario_especial(eleccion_materias,
                eleccion_materias_por_grupo, inicio, fin)
                num = 1
                try:
                    for horario in opciones:
                        print('\n{}Opción{}{}'.format('#'*20,num,'#'*20))
                        num += 1
                        horario_toStr(horario)
                except Exception:
                    print('No hay horarios disponibles con esa elección')

    frame_horario = Frame(top)
    frame_horario.grid(row=3,columnspan=3)
    try:
        frames[0].destroy()
        if frames[1] != '':
            frames[1].destroy()
    except Exception:
        pass
    frames[0] = frame_horario

    reloj_inicio = App(frame_horario)
    reloj_inicio.grid(row=1,column=0)
    inicio_label = Label(frame_horario,text='Hora de inicio')
    inicio_label.grid(row=0,columnspan=2)
    #inicio_button = Button(frame_horario,command=lambda : registrar_hora('inicio',reloj_inicio),
    #                        text='Registrar',bg='green')
    #inicio_button.grid(row=1,column=1)


    reloj_fin = App(frame_horario)
    reloj_fin.grid(row=3,column=0)
    fin_label = Label(frame_horario,text='Hora de termino')
    fin_label.grid(row=2,columnspan=2)

    warning_label = Label(text='',font=helv8)
    fin_button = Button(frame_horario, command= lambda : registrar_hora('fin',reloj_inicio,reloj_fin,warning_label),
                        text='Registrar',bg='green')    
    fin_button.grid(row=3,column=1)
    warning_label.grid(row=4,columnspan=2)

    warning_label2 = Label(text='',font=helv8)
    warning_label2.grid(row=4,column=2,columnspan=2)
    crear_horario_button = Button(frame_horario,text='Crear horario', bg='yellow', command=lambda : hacer_horario(warning_label2))
    crear_horario_button.grid(column=4,row=3)
    


#https://stackoverflow.com/questions/57034118/time-picker-for-tkinter
class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'6')
        self.hour = tk.Spinbox(self,from_=6,to=22,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'0')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
        self.hour.grid()
        #self.min.grid(row=0,column=1)

    def trace_var(self,*args):
        #if self.last_value == "59" and self.minstr.get() == "0":
         #   self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.hourstr.get()






boton1 = Button(top, bg='#58CACA',text='Semestres',command=semestres)
boton1.grid(column=0,row=1)

boton2 = Button(top, bg='#58CACA',text='Crear Horarios',command=crear_horario_window)
boton2.grid(column=2,row=1)

boton3 = Button(top, bg='#58CACA',text='Recomendador de optativas',command=recomendador_optativas_window)
boton3.grid(column=1,row=1)
#for row_num in range(top.grid_size()[1]):
#    top.rowconfigure(row_num, weight=1)

#for col_num in range(top.grid_size()[0]):
#    top.columnconfigure(col_num, weight=1)


top.mainloop()
