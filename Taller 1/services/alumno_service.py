from repository.database import BaseDatos

class AlumnoService:
    @staticmethod
    def crear(alumno):
        BaseDatos.alumnos[alumno.rut] = alumno
        print(f"[DB] Alumno {alumno.nombre} agregado")

    @staticmethod
    def recuperar(rut):
        return BaseDatos.alumnos.get(rut)

    @staticmethod
    def modificar(rut, nuevo_nombre):
        if rut in BaseDatos.alumnos:
            BaseDatos.alumnos[rut].nombre = nuevo_nombre
            print(f"[DB] Alumno {rut} modificado")

    @staticmethod
    def eliminar(rut):
        if rut in BaseDatos.alumnos:
            del BaseDatos.alumnos[rut]
            print(f"[DB] Alumno {rut} eliminado")
