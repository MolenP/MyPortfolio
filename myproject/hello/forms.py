from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=False)
    password = forms.CharField(label="Пароль", min_length=8)