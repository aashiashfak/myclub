# # base/forms.py 
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
# from django import forms
# from django.forms.widgets import PasswordInput, TextInput



# class CreateUserForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(CreateUserForm, self).__init__(*args, **kwargs)
#         self.fields['username'].help_text = ''  # Remove username help text
#         self.fields['password1'].help_text = ''  # Remove password1 help text
#         self.fields['password2'].help_text = ''  # Remove password2 help text

# class LoginForm(AuthenticationForm):

#     username = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())

# base/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
import re

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Remove username help text
        self.fields['password1'].help_text = ''  # Remove password1 help text
        self.fields['password2'].help_text = ''  # Remove password2 help text

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        if not username.isalnum():
            raise forms.ValidationError("Username must contain only alphanumeric characters")
        if len(username) >= 12:
            raise forms.ValidationError("Enter at least 12 characters")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            raise forms.ValidationError("This field is required")
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_regex.match(email):
            raise forms.ValidationError("Invalid email format")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')

        if not password1:
            raise forms.ValidationError("This field is required")

        if len(password1) < 8:
            raise forms.ValidationError("This password is too short. It must contain at least 8 characters.")
        
        if not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1):
            raise forms.ValidationError("Password must contain numbers and characters") 
        
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return password2


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("User does not exist. Please sign up.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("This field is required")
        return password