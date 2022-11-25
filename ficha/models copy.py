
from django.db import models


class Comentario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha_comentario = models.DateField()
    hora_comentario = models.TimeField()
    estado = models.CharField(db_column='Estado', max_length=20)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=300)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_funcionario')

    class Meta:
        managed = False
        db_table = 'comentario'


class Comuna(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_region = models.CharField(max_length=35)
    id_region = models.OneToOneField('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'





class Ficha(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_comentario = models.ForeignKey(Comentario, models.DO_NOTHING, db_column='id_comentario')
    id_ingreso = models.OneToOneField('Ingreso', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ficha'





class Ingreso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha_comentario = models.DateField()
    hora_comentario = models.TimeField()
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    

    class Meta:
        managed = False
        db_table = 'ingreso'




class Patologia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_patologia = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'patologia'


class Region(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_region = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'region'


class Rol(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_rol = models.CharField(max_length=20)
    lectura = models.BooleanField() # This field type is a guess.
    escritura = models.BooleanField()  # This field type is a guess.
    borrar = models.BooleanField()  # This field type is a guess.
    crear = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rol'


class Sintomas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_sintoma = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'sintomas'





// Nueva Tabla

class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rut = models.CharField(unique=True, max_length=15)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    contrasenia = models.CharField(max_length=80)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol', default=3)

    class Meta:
        managed = False
        db_table = 'usuario'

class 

class Paciente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sexo_biologico = models.CharField(max_length=20)
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_rol = models.OneToOneField('Rol', models.DO_NOTHING, db_column='id_rol')
    id_comuna = models.OneToOneField(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_sintoma = models.OneToOneField('Sintomas', models.DO_NOTHING, db_column='id_sintoma')

    class Meta:
        managed = False
        db_table = 'paciente'

class Familiar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relacion_paciente = models.CharField(max_length=30)
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_rol = models.OneToOneField('Rol', models.DO_NOTHING, db_column='id_rol')
    id_comuna = models.OneToOneField(Comuna, models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'familiar'

class Funcionario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cargo = models.CharField(max_length=30)
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_rol = models.OneToOneField('Rol', models.DO_NOTHING, db_column='id_rol')
    id_comuna = models.OneToOneField(Comuna, models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'funcionario'