from django import forms

class PrestamoForm(forms.Form):
    socio = forms.CharField(label='Socio', max_length=8, required=True)
    isbn = forms.CharField(label='ISBN', max_length=13, required=True)