from django import forms
from .models import User, Message


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter your message", 'rows': 3})
        }