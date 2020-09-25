from django.db import models
from django.core.validators import (MaxLengthValidator,
                                    MinValueValidator,
                                    MinLengthValidator,
                                    RegexValidator)

from escuela.models import Alumno

LONGUITUD_MAXIMA = 'Error en la longitud'
LONGUITUD_MAXIMA_SALDO = 'Error en la longitud son 9 digitos los permitidos'
LONGITUD_MINIMA = 'Error de longitud mínima'
VALOR_MINIMO = 'El valor mínimo permitido es 32'
VALOR_MAXIMO_LOC = 'El valor máximo permitido son 1000'
VALOR_MAXIMO_DOM = 'El valor máximo permitido son 9999'
VALOR_MAXIMO = 'El valor máximo permitido son 100'
VALOR_MAXIMO_UBI = 'El valor máximo permitido son 999000000'
FORMATO_NUMERO_INCORRECTO = 'Formato inválido no deben ir numéros'
FORMATO_CARACTER_INCORRECTO = 'Formato sólo se aceptan letras :'


regexNumero = RegexValidator('^[0-9]*$', 'No se permiten letras')
regexCaracter = RegexValidator(
    r"^[A-Za-zÀ-ÿ\u00E0-\u00FC ]+$", 'No se permiten caracteres especiales')


class Grupo(models.Model):
    total = models.IntegerField(
        "Total grupos:",
        default=0,
        validators=[
            MaxLengthValidator(9999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    alumno = models.ForeignKey(
        Alumno, verbose_name="Alumnos",
        on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return self.total

class Docentes(models.Model):
    total_docentes = models.IntegerField(
        "Total Docentes:",
        default=0,
        validators=[
            MaxLengthValidator(9999,LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    mujeres_docentes = models.IntegerField(
        "Mujeres:",
        default=0,
        validators=[
            MaxLengthValidator(999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    hombres_docentes = models.IntegerField(
        "Hombres:",
        default=0,
        validators=[
            MaxLengthValidator(999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    grupo = models.ForeignKey(
        Grupo, verbose_name="Grupo",
        on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.total_docentes

class Periodo (models.Model):
    periodo = models.CharField(
        max_length=9, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(9,LONGUITUD_MAXIMA),
            MinLengthValidator(9,LONGITUD_MINIMA),regexCaracter])

    tipo_educativo = models.CharField(
        max_length=30, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(30,LONGUITUD_MAXIMA),
            MinLengthValidator(12,LONGITUD_MINIMA)])

    nivel_educativo = models.CharField(
        max_length=12, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(12,LONGUITUD_MAXIMA),
            MinLengthValidator(8,LONGITUD_MINIMA)])

    servicio_educativo = models.CharField(
        max_length=30, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(30,LONGUITUD_MAXIMA),
            MinLengthValidator(5,LONGITUD_MINIMA),regexCaracter])

    grupo = models.ForeignKey(
        Grupo, verbose_name="Grupo",
        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nivel_educativo

class Salones(models.Model):
    aulas_existentes = models.IntegerField(
        max_length=999, null=False, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    aulas_uso = models.IntegerField(
        max_length=999, null=False, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    laboratorios = models.IntegerField(
        max_length=999, null=False, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    talleres = models.IntegerField(
        max_length=999, null=False, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    grupo = models.ForeignKey(
        Grupo, verbose_name="Grupo",
        on_delete=models.CASCADE, null=True, blank=True)