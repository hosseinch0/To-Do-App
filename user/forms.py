from django import forms
from django.contrib.auth.models import User


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
