from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppTraveling.models import *

class viajeroForm(forms.Form):
    
    nombre   = forms.CharField()
    apellido = forms.CharField()
    correo   = forms.EmailField()
    destino  = forms.CharField() 
    edad     = forms.IntegerField()
    adulto   = forms.BooleanField()

class destinoForm (forms.Form):
    
    nombre     = forms.CharField()
    comentario = forms.CharField()

class alojamientoForm (forms.Form):
    
    nombre                = forms.CharField()
    ubicacion             = forms.CharField()
    cantidad_habitaciones = forms.IntegerField()
    cantidad_personas     = forms.IntegerField()
    mascotas              = forms.BooleanField()

class vuelosForm (forms.Form):
    
    numero                = forms.IntegerField()
    destino               = forms.CharField()
    origen                = forms.CharField()
    salida                = forms.DateField()
    llegada               = forms.DateField()
    cantidad_pasajes      = forms.IntegerField()
    empresa               = forms.CharField()

###Registro

class RegistroFormulario(UserCreationForm):
    
    F_nacimiento = forms.DateField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        help_texts= {i:"" for i in fields}

##Cambiar datos de registro

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['email','password1','password2']
        help_texts= {k:"" for k in fields}
