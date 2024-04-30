from django.db import models

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField(null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now_add=True)
    creado_por = models.CharField(max_length=50)
    direccion = models.OneToOneField('Direccion', on_delete=models.SET_NULL, null=True, blank=True)
    curso = models.ManyToManyField('Curso', related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.curso}"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    version = models.IntegerField()
    profesores = models.ManyToManyField('Profesor', related_name='cursos')

    def __str__(self):
        return f"{self.nombre} v{self.version}"

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now_add=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
