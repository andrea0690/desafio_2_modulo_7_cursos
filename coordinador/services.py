from django.core.exceptions import ObjectDoesNotExist
from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(codigo, nombre, version):
    curso = Curso.objects.filter(codigo=codigo)
    if curso.exists():
        return curso.first()
    curso = Curso.objects.create(
        codigo=codigo,
        nombre=nombre,
        version=version
    )
    return curso


def crear_profesor(rut, nombre, apellido, activo=True):
    profesor = Profesor.objects.filter(rut=rut)
    if profesor.exists():
        return profesor.first()
    profesor = Profesor.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo
    )
    return profesor


def crear_estudiante(rut, nombre, apellido, fecha_nacimiento, direccion=None, activo=True):
    estudiante = Estudiante.objects.filter(rut=rut)
    if estudiante.exists():
        return estudiante.first()
    estudiante = Estudiante.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        direccion=direccion,
        activo=activo
    )
    return estudiante


def crear_direccion(calle, numero, comuna, ciudad, region, dpto=None):
    direccion = Direccion.objects.create(
        calle=calle,
        numero=numero,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region
    )
    return direccion


def obtiene_estudiante(rut):
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        return estudiante
    except ObjectDoesNotExist:
        print(f"Estudiante con RUT {rut} no encontrado")
        return None


def obtiene_profesor(rut):
    try:
        profesor = Profesor.objects.get(rut=rut)
        return profesor
    except ObjectDoesNotExist:
        print(f"Profesor con RUT {rut} no encontrado")
        return None


def obtiene_curso(codigo):
    try:
        curso = Curso.objects.get(codigo=codigo)
        return curso
    except ObjectDoesNotExist:
        print(f"Curso con código {codigo} no encontrado")
        return None
    
def obtiene_direccion(id):
    try:
        dir = Direccion.objects.get(id=id)
        return dir
    except ObjectDoesNotExist:
        print(f"Direccion con id {id} no encontrado")
        return None

def agrega_profesor_a_curso(curso:Curso, profesor:Profesor):
    curso.profesores.add(profesor)  
    curso.save()  


def agrega_cursos_a_estudiante(estudiante:Estudiante, curso:Curso):
    estudiante.curso.add(curso) 
    estudiante.save()  
    imprime_estudiante_cursos(estudiante.rut)


def imprime_estudiante_cursos(rut):
    estudiante = obtiene_estudiante(rut)
    if estudiante:
        print(f"Estudiante: {estudiante.nombre} {estudiante.apellido}")
        cursos = estudiante.curso.all()
        for c in cursos:
            print("     Curso:")
            print(f"        - {c.codigo} {c.nombre}")
            profesores = c.profesores.all()
            print("     Profesores:")
            for p in profesores:
                print(f"        - {p.nombre} {p.apellido}")
    else:
        print(f"No se encontró el estudiante con RUT {rut}")
