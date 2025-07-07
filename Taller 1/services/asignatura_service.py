from repository.database import BaseDatos

class AsignaturaService:
    @staticmethod
    def crear(asignatura):
        BaseDatos.asignaturas[asignatura.codigo] = asignatura
        print(f"[DB] Asignatura {asignatura.nombre} agregada")

    @staticmethod
    def recuperar(codigo):
        return BaseDatos.asignaturas.get(codigo)

    @staticmethod
    def modificar(codigo, nuevo_nombre):
        if codigo in BaseDatos.asignaturas:
            BaseDatos.asignaturas[codigo].nombre = nuevo_nombre
            print(f"[DB] Asignatura {codigo} modificada")

    @staticmethod
    def eliminar(codigo):
        if codigo in BaseDatos.asignaturas:
            del BaseDatos.asignaturas[codigo]
            print(f"[DB] Asignatura {codigo} eliminada")
