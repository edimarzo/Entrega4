from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django import forms


class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label='Usuario') 
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput)  

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("No coinciden las contraseñas")  
        return password2  
    
class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    url = forms.URLField(label='Página Web',required=False)
    
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','url','avatar']