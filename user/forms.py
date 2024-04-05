from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255, required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(required=True, min_length=8)
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=False)
