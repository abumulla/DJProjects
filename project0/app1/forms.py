from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=250)
    age = forms.IntegerField()
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __str__(self):
        return self.email
