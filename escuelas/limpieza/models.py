from django.db import models
from django.db import models
from django.core.validators import (MaxLengthValidator,
                                    MinValueValidator,
                                    MinLengthValidator,
                                    RegexValidator)

from grupo.models import Salones

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

class Limpieza(models.Model):

    salones = models.ForeignKey(
        Salones, verbose_name="Salones",
        on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.fecha_limpeza

class Personal(models.Model):
    total_personal = models.IntegerField(
        "Total Personal:",
        default=0,
        validators=[
            MaxLengthValidator(9999,LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    mujeres_personal = models.IntegerField(
        "Mujeres:",
        default=0,
        validators=[
            MaxLengthValidator(999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    hombres_personal = models.IntegerField(
        "Hombres:",
        default=0,
        validators=[
            MaxLengthValidator(999,LONGUITUD_MAXIMA),
            MinLengthValidator(0,LONGITUD_MINIMA),regexCaracter])

    limpieza = models.ForeignKey(
        Limpieza, verbose_name="Limpieza",
        on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.total_personal




