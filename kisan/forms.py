from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact,Detail_item,Address,Thing
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label=('Password'),widget=forms.PasswordInput())
    password2 =forms.CharField(label=('Re-Enter Password'),widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']



class LoginForm(AuthenticationForm):
    username=UsernameField(label="Username",widget=forms.TextInput())
    password=forms.CharField(label=("Password"),widget=forms.PasswordInput())
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'query':forms.Textarea(attrs={'class':'form-control'}),
        }
class Detail_itemForm(forms.ModelForm):
    class Meta:
        model=Detail_item
        fields='__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'
        labels={
            'name':'Enter complete name',
            'mobile':'Enter Phone Number ',
            'address':'Enter Complete address'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
        }
class ThingForm(forms.ModelForm):
    class Meta:
        model=Thing
        fields='__all__'
        labels={
            'name':'Enter Product Name',
            'desc':'Enter Description',

                    }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
