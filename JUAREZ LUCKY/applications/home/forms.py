from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellidos = forms.CharField(max_length=100, required=True)
    numero_celular = forms.CharField(max_length=15, required=True)
    cantidad = forms.IntegerField(min_value=1, max_value=100, required=True)
