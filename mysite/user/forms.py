from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','password','email')
    
    def clean_username(self):
        data = self.cleaned_data.get('username')
        if "@" in data:
            raise forms.ValidationError("Contains @")
        return data