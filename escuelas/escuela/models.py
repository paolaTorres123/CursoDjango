from django.db import models
from django.core.validators import (MaxLengthValidator,
                                    MinValueValidator,
                                    MinLengthValidator,
                                    RegexValidator)

from entidad.models import Domicilio

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

class Escuela(models.Model):
    clave_escuela = models.CharField(
        max_length=10, null=False, blank=False, 
        default='',
        validators=[
            MaxLengthValidator(10,LONGUITUD_MAXIMA),
            MinLengthValidator(10,LONGUITUD_MAXIMA)])

    turno_escuela = models.CharField(
        max_length=30, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(30,LONGUITUD_MAXIMA),
            MinLengthValidator(6, LONGITUD_MINIMA),regexNumero])

    ambito_escuela = models.CharField(
        max_length=6, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(6,LONGUITUD_MAXIMA),
            MinLengthValidator(5,LONGITUD_MINIMA)])
    
    centro_educativo = models.CharField(
        max_length=80, null=False, blank=False,
        default='',
        validators=[
           MaxLengthValidator(80,LONGUITUD_MAXIMA),
           MinLengthValidator(5,LONGITUD_MINIMA)])

    control_escuela = models.CharField(
        max_length=8, null=False, blank=False,
        default='',
        validators=[
            MaxLengthValidator(8, LONGUITUD_MAXIMA),
            MinLengthValidator(6,LONGITUD_MINIMA),regexNumero])
    
    domicilio = models.ForeignKey(
        Domicilio, verbose_name="Domicilio",
        on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return self.centro_educativo

class Contacto(models.Model):
    lada = models.IntegerField(
        max_length=4, null=True, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(4,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    telefono = models.IntegerField(
        max_length=5, null=True, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(5,LONGUITUD_MAXIMA),
            MinLengthValidator(0, LONGITUD_MINIMA),regexCaracter])

    correo_electronico = models.CharField(
        max_length=50, null=True, blank=False,
        default=0,
        validators=[
            MaxLengthValidator(50, LONGUITUD_MAXIMA),
            MinLengthValidator(15,LONGITUD_MINIMA)])

    escuela = models.ForeignKey(
        Escuela, verbose_name="Escuela",
        on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.correo_electronico



class Alumno(models.Model):
    total_alumnos = models.IntegerField(
        "Total Alumnos:",
        default=0,
        validators=[
            MaxLengthValidator(9999,LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    mujeres_alumnas = models.IntegerField(
        "Mujeres:",
        default=0,
        validators=[
            MaxLengthValidator(999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    hombres_alumnos = models.IntegerField(
        "Hombres:",
        default=0,
        validators=[
            MaxLengthValidator(999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    escuela = models.ForeignKey(
        Escuela, verbose_name="Escuela",
        on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.total_alumnos

