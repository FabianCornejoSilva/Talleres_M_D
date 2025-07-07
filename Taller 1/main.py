from models.alumno import EstudianteMagister
from models.alumno import EstudianteNoAyudante
from models.alumno import EstudianteAyudante
from models.alumno import EstudianteDoctorado
from models.asignatura import Asignatura
from services.alumno_service import AlumnoService
from services.asignatura_service import AsignaturaService

if __name__ == "__main__":
    estudiante = EstudianteMagister("Fabian", 21, "12345678-9", "2003-05-12")
    AlumnoService.crear(estudiante)

    estudiante1 = EstudianteNoAyudante("Neil", 21, "12345678-9", "2003-05-12")
    AlumnoService.crear(estudiante1)

    estudiante2 = EstudianteAyudante("Juan", 21, "12345678-9", "2003-05-12")
    AlumnoService.crear(estudiante2)

    estudiante3 = EstudianteDoctorado("Pablo", 21, "12345678-9", "2003-05-12")
    AlumnoService.crear(estudiante3)

    ramo = Asignatura("Diseño Software", "DSW001", 6, "magister")
    AsignaturaService.crear(ramo)

    #EstudianteMagister
    estudiante.agregar_asignatura(ramo)
    estudiante.estudiar()
    estudiante.hacer_ayudantia()
    estudiante.hacer_clases()
    estudiante.investigar()
    estudiante.descargar_notas()
    #EstudianteNoAyudante
    estudiante1.agregar_asignatura(ramo)
    estudiante1.estudiar()
    estudiante1.hacer_ayudantia()
    estudiante1.hacer_clases()
    estudiante1.investigar()
    estudiante1.descargar_notas()
    #EstudianteAyudante
    estudiante2.agregar_asignatura(ramo)
    estudiante2.estudiar()
    estudiante2.hacer_ayudantia()
    estudiante2.hacer_clases()
    estudiante2.investigar()
    estudiante2.descargar_notas()
    #EstudianteDoctorado
    estudiante3.agregar_asignatura(ramo)
    estudiante3.estudiar()
    estudiante3.hacer_ayudantia()
    estudiante3.hacer_clases()
    estudiante3.investigar()
    estudiante3.descargar_notas()
