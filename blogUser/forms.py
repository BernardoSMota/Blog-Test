from django import forms
from blogUser.models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

class customUserForm(forms.ModelForm):    
    class Meta:       
        model = CustomUser
        fields = ['username', 'email', 'profile_picture', 'first_name', 'last_name', 'super_user_code', 'password1', 'password2']
                    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label="Senha",
        help_text=password_validation.password_validators_help_text_html()
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label="Confirmar Senha",
    )


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        try:
            password_validation.validate_password(password1)

        except ValidationError as errors:
            self.add_error('password1', ValidationError(errors))

        return password1

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            self.add_error('password2', ValidationError('As senhas não coincidem'))
            
        return super().clean()