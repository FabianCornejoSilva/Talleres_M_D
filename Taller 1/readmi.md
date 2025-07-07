# Taller Práctico 1 - Principios SOLID

## Supuestos
- Se simula persistencia con diccionarios.
- Las notas se representan como texto simulado.
- Las asignaturas pueden pertenecer a un tipo (pregrado, magíster, doctorado), pero no se valida compatibilidad al inscribir.

## Principios SOLID aplicados
- SRP: Separación de responsabilidades en clases, servicios y repositorios.
- OCP: Nuevos tipos de alumnos pueden agregarse sin modificar los existentes.
- LSP: Subclases de `Alumno` pueden ser usadas sin romper la lógica.
- ISP: Interfaces pequeñas para actividades (`Actividad`).
- DIP: Clases dependen de abstracciones (servicios, no directamente de base de datos).
