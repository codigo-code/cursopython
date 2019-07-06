# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#metodo inciial
def inicio():
    nombre ="Dante Panella"
    edad = 36
    print (nombre , " " , edad)
    
    print (type(edad))
    
    def fullName():
        return nombre + " " , edad
    
    def imc(altura,peso):
        return peso/(altura*altura)
    
    
    def metodoSarasa():
        print( 2+1)
        nombre="pepito"
        
        
    print (fullName())
    
    
    print(imc(1.94,109))
    
    
    def calcularRotura(imc):
        
        if(imc < 18):
            print("esta flaco")
        elif(imc >= 18 and imc < 25):
            print ("estas en tu peso ideal")
        else:
            print ("alfoja a la achura")
    
    
    print(calcularRotura(imc(1.74,84)))

if(__name__ =="__main__"):
    print ("inicio de la aplicaicon")
    inicio()


class Persona:
    
   #Constructor
   def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad


class Curso:

    #Esto es un comentario
    def __init__(self,nombre,horario):
        self.nombre=nombre
        self.horario=horario
        self.materias=[]
        
        
    def getNombreCursada(self):
        return self.nombre
    
    def addMatetria(self,nombreMateria):
        self.materias.append(nombreMateria)
        
    def showMateria(self):
        for materia in self.materias:
            print(materia)
        


class Estudiante(Persona,Curso):

    def __init__(self,curso,legajo,nombre,apellido,edad,nombreCursada,horario):
        self.curso=curso
        self.legajo=legajo
        Persona.__init__(self,nombre,apellido,edad)
        Curso.__init__(self,nombreCursada,horario)
    




p1 = Persona("Dante","Panella",37)
e1 = Estudiante("curso python",1234, "Nicolas","Neme",41, "Python inicial", "9 a 13 hs" )

print (e1.nombre + " esta cursando " + e1.getNombreCursada())





