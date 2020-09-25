from .models import(Contacto,Alumno,Domicilio,Escuela,LONGUITUD_MAXIMA,
                    LONGITUD_MINIMA,FORMATO_CARACTER_INCORRECTO,FORMATO_NUMERO_INCORRECTO,
                    VALOR_MAXIMO,VALOR_MINIMO)
from django.forms import ModelForm, TextInput, NumberInput


class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = "__all__"

        widgets = {
            'clave_escuela': TextInput(attrs={'class': 'form-control input-form'}),
            'turno_escuela': TextInput(attrs={'class': 'form-control input-form'}),
            'ambito_escuela': TextInput(attrs={'class': 'form-control input-form'}),
            'centro_educativo':TextInput(attrs={'class': 'form-control input-form'}),
            'control_escuela':TextInput(attrs={'class': 'form-control input-form'}),            
        }
        error_messages = {
            'clave_escuela':{
                'max_length': LONGUITUD_MAXIMA,
                'required': 'La clave de la escuela es requerida.'
            },
            'turno_escuela':{
                'max_length':LONGUITUD_MAXIMA,
                'requiered': 'El turno es requerido'
            },
            'ambito_escuela': {
                'max_length':LONGUITUD_MAXIMA,
                'requiered': 'El ambito es requerido'
            },
            'centro_educativo': {
                'max_length':LONGUITUD_MAXIMA,
                'requiered': 'El centro educativo es requerido'
            },
            'control_escuela': {
                'max_length':LONGUITUD_MAXIMA,
                'requiered': 'El control es requerido'
            },
        }
class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        exclude = ['escuela']

        widgets = {
            'lada': NumberInput(attrs={'class': 'form-control'}),
            'telefono': NumberInput(attrs={'class': 'form-control'}),
            'correo_electronico': TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'lada':{
                'max_length':LONGITUD_MINIMA
            },
            'telefono':{
                'max_length':LONGITUD_MINIMA

            },
        }
class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        exclude = ['escuela','Ubicacion']

        widgets = {
            'nombre_domicilio': TextInput(attrs={'class': 'form-control'}),
            'numero_externo': TextInput(attrs={'class': 'form-control'}),
        }
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        exclude = ['escuela']

        widgets = {
           'total_alumnos' : NumberInput(attrs={'class': 'form-control'}),
           'mujeres_alumnas' : NumberInput(attrs={'class': 'form-control'}),
           'hombres_alumnos' : NumberInput(attrs={'class': 'form-control'}),
        }
