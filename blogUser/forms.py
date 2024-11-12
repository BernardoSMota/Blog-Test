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
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Email já cadastrado'))
        return email



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
    
class editUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'profile_picture', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.profile_picture:
            self.fields['profile_picture'].widget = forms.ClearableFileInput(attrs={'class': 'custom-file-input'})

    
    def clean_email(self):
        current_email = self.instance.email
        email = self.cleaned_data.get('email')
        
        if CustomUser.objects.filter(email=email).exists() and current_email != email:
            self.add_error('email', ValidationError('Email já cadastrado'))            
        return email
    
class passwordEditForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
    
    class Meta:   
        model = CustomUser
        fields = ['password', 'password1', 'password2']
       
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label="Senha Atual",
    )
       
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label="Nova Senha",
        help_text=password_validation.password_validators_help_text_html()
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label="Confirmar Senha",
    )
    
    
    def clean_password(self):
        current_password = self.cleaned_data.get('password')
        if not self.user.check_password(current_password):
            raise ValidationError("A senha atual está incorreta.")
        
        
        return current_password
    
    
    def clean_password1(self):
        current_password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
    
        try:
            password_validation.validate_password(password1)

        except ValidationError as errors:
            self.add_error('password1', ValidationError(errors))
            
        if current_password == password1:
            self.add_error('password1', 'A nova senha deve ser diferente da senha atual')
            

        return password1
    
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise ValidationError('Senhas não coincidem')
        
        
        return password2