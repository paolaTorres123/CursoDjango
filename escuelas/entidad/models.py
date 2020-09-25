from django.db import models
from django.core.validators import (MaxLengthValidator,
                                    MinValueValidator,
                                    MinLengthValidator,
                                    RegexValidator)

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


class Entidad(models.Model):
    clave_entidad = models.IntegerField(
        "Clave Entidad:",
        default=32,
        validators=[
            MinLengthValidator(32,VALOR_MINIMO),
            MaxLengthValidator(32)])

    nombre_entidad = models.CharField(
        max_length=30, null=False, blank=False, 
        default='',
        validators=[
            MaxLengthValidator(30, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter])

    

    def __str__(self):
        return self.nombre_entidad

class Municipio(models.Model):
    clave_municipio = models.IntegerField(
        "Clave Municipio:",
        default=0,
        validators=[
            MinLengthValidator(0,VALOR_MINIMO),
            MaxLengthValidator(100, VALOR_MAXIMO)])

    nombre_municipio= models.CharField(
        max_length=30, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(30, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter]) 

    entidad = models.ForeignKey(
        Entidad, verbose_name="Entidad",
        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre_municipio

class Localidad(models.Model):
    clave_localidad = models.IntegerField(
       "Clave Localidad:",
        default=0,
        validators=[
            MinLengthValidator(0,VALOR_MINIMO),
            MaxLengthValidator(1000, VALOR_MAXIMO_LOC)])

    nombre_localidad = models.CharField(
        max_length=50, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(50, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter])

    entidad = models.ForeignKey(
        Entidad, verbose_name="Entidad",
        on_delete=models.CASCADE, null=True, blank=True)

    

class Domicilio(models.Model):
    nombre_domicilio = models.CharField(
        max_length=50, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(50, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter])
    numero_externo = models.CharField(
        max_length=30, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(30, LONGUITUD_MAXIMA),
            MinLengthValidator(1, LONGITUD_MINIMA)])

    entidad = models.ForeignKey(
        Entidad, verbose_name="Entidad",
        on_delete=models.CASCADE, null=True, blank=True)

class Ubicacion(models.Model):
    altitud_msnm = models.IntegerField(
        default=0,
        validators=[
            MinLengthValidator(0,VALOR_MINIMO),
            MaxLengthValidator(9999, VALOR_MAXIMO_DOM)])
    longitud = models.DecimalField(
        max_digits=14,
        decimal_places=10,
        default=0,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(999000000, VALOR_MAXIMO_UBI)])
    latitud = models.DecimalField(
        max_digits=12,
        decimal_places=8,
        default=0,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(999000000, VALOR_MAXIMO_UBI)])

    longitud_gms = models.CharField(
        max_length=20, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(20, LONGUITUD_MAXIMA),
            MinLengthValidator(16, LONGITUD_MINIMA)])

    latitud_gms = models.CharField(
        max_length=8, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(8),
            MinLengthValidator(7)])
    
    entidad = models.ForeignKey(
        Entidad, verbose_name="Entidad",
        on_delete=models.CASCADE, null=True, blank=True)


    domicilio = models.ForeignKey(
        Domicilio,verbose_name="Docimiclio",
        on_delete=models.CASCADE, null=True, blank=True)

    
    

    
    

     