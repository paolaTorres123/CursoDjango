from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    emial = forms.EmailField(label="Email",required=True)
    contect = forms.CharField(label="Contenido",required=True, widget=forms.Textarea)