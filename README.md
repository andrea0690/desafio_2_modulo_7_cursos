## CAPTURAS
Las capturas se encuentran en el archivo requerimientos.pdf dentro de la carpeta requerimientos

# CURSOS- Proyecto Django

Este proyecto tiene como objetivo proporcionar instrucciones paso a paso para crear y gestionar un proyecto en Django. A continuación se describen los modelos de cursos, estudiantes y profesores involucradas en el proceso.

Desafio Dia 4 - Modulo 7 shell


## Lista de Instrucciones

### Importación Inicial
Para comenzar la shell de django, ejecuta el siguiente comando:
```
python3 manage.py shell
```

Para comenzar, importa todas las funciones del archivo `services.py`:
```python
from desafioadl.services import *
```


### Ejecutación de instrucciones
creacion de cursos
```python
curso_javascript = crear_curso("JS101", "Curso de Javascript Básico", 1)
curso_java = crear_curso("JV101", "Curso de Java Básico", 1)
```

Creación de profesores
```python
profesor_carlos=crear_profesor("11111", "Carlos", "Perez")
profesor_miguel=crear_profesor("22222", "Miguel", "Guerra")
```

creacion de estudiantes
```python
andrea = crear_estudiante("33333","Andrea","Pérez","2000-01-01")
pedro = crear_estudiante("44444","Pedro","Marcano","2002-12-01")
```

creacion de crear_direccion
```python
dir = crear_direccion("Vicuña Mackenna", "123", "Santiago", "Santiago", "Metropolitana", "50")
```

Agregar profesores a cursos
```python
agrega_profesor_a_curso(curso_java, profesor_miguel)
agrega_profesor_a_curso(curso_javascript, profesor_carlos)
agrega_profesor_a_curso(curso_javascript, profesor_miguel)
```

agrega cursos a estudiantes
```python
agrega_cursos_a_estudiante(andrea, curso_java)
Estudiante: Andrea Pérez
     Curso:
        - JV101 Curso de Java Básico
     Profesores:
        - Miguel Guerra
agrega_cursos_a_estudiante(andrea, curso_javascript)
Estudiante: Andrea Pérez
     Curso:
        - JV101 Curso de Java Básico
     Profesores:
        - Miguel Guerra
     Curso:
        - JS101 Curso de Javascript Básico
     Profesores:
        - Carlos Perez
        - Miguel Guerra
```

obtiene curso python y se agrega a estudiante pedro
```python
curso_python = obtiene_curso("PY101")
agrega_cursos_a_estudiante(pedro, curso_python)
Estudiante: Pedro Marcano
     Curso:
        - PY101 Curso de Python Básico
     Profesores:
```

Se agrega profesor miguel a curso python
```python
agrega_profesor_a_curso(curso_python, profesor_miguel)
```

Imprime cursos de estudiante con rut 44444, 33333 y un rut que no existe
```python
imprime_estudiante_cursos("44444")
Estudiante: Pedro Marcano
     Curso:
        - PY101 Curso de Python Básico
     Profesores:
        - Miguel Guerra
        
imprime_estudiante_cursos("33333")
Estudiante: Andrea Pérez
     Curso:
        - JV101 Curso de Java Básico
     Profesores:
        - Miguel Guerra
     Curso:
        - JS101 Curso de Javascript Básico
     Profesores:
        - Carlos Perez
        - Miguel Guerra

imprime_estudiante_cursos("rutRARO")
Estudiante con RUT rutRARO no encontrado
No se encontró el estudiante con RUT rutRARO
```