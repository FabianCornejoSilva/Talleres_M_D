from abc import ABC, abstractmethod

class Alumno:
    def __init__(self, nombre, edad, rut, fecha_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def descargar_notas(self):
        print(f"Notas de {self.nombre}: [Simulación de notas por asignatura]")
        
class IEstudiar(ABC):
    @abstractmethod
    def estudiar(self): pass

class IAyudantia(ABC):
    @abstractmethod
    def hacer_ayudantia(self): pass

class IClases(ABC):
    @abstractmethod
    def hacer_clases(self): pass

class IInvestigacion(ABC):
    @abstractmethod
    def investigar(self): pass

class Titulado(Alumno, IEstudiar):
    def estudiar(self): pass

class EstudianteNoAyudante(Alumno, IEstudiar):
    def estudiar(self): print(f"{self.nombre} está estudiando.")
    def hacer_ayudantia(self): pass
    def hacer_clases(self): pass
    def investigar(self): pass

class EstudianteAyudante(EstudianteNoAyudante, IAyudantia):
    def hacer_ayudantia(self): print(f"{self.nombre} hace ayudantía.")

class EstudianteMagister(EstudianteAyudante, IClases):
    def hacer_clases(self): print(f"{self.nombre} hace clases.")

class EstudianteDoctorado(EstudianteMagister, IInvestigacion):
    def investigar(self): print(f"{self.nombre} investiga.")

