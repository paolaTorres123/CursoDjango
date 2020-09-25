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


class Equipo(models.Model):

    salones = models.ForeignKey(
        Salones, verbose_name="Salones",
        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.computadoras

class Computadoras(models.Model):
    computadoras_operacion = models.IntegerField(
        "Computadoras en operacion",
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    computadoras_operacion_internet = models.IntegerField(
        "Computadoras en operacion con internet",
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    computadoras_operacion_uso_educativo = models.IntegerField(
        "Computadoras en operacion con internet",
        default=0,
        validators=[
            MaxLengthValidator(999, LONGUITUD_MAXIMA),
            MinLengthValidator(1,LONGITUD_MINIMA),regexCaracter])

    equipo = models.ForeignKey(
        Equipo, verbose_name="Equipo",
        on_delete=models.CASCADE, null=True, blank=True)
