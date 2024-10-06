from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label="")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),label="")
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),label="")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
      
          

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
    
    def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])  # Hash the password
            if commit:
                user.save()
            return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label="")