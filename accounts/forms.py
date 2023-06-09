from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm


class CustomAuthentication(AuthenticationForm):
    username = forms.CharField(
        label= '아이디',
        widget= forms.TextInput(attrs={'class':'form-control',}),
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class':'form-control',}),
    )
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'email': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'first_name': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'last_name': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
        }
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)