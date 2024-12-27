from django import forms
from .models import Task,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.forms import inlineformset_factory

class AddTask(forms.ModelForm):
    class Meta:
        model=Task
        fields = ['title', 'description', 'due_date']
       
        labels={
            'title':'name'
        }
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter Task Title','fonrt-size':'1.4vw'}),
            'due_date':forms.DateInput(attrs={'type': 'date'}),
   

        }
        error_messages = {
            'due_date': {
                'required': 'Price is mandatory.',
                'invalid': 'Enter a valid price.',
            }
        }

class editForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title', 'description', 'due_date']
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter Task Title','fonrt-size':'1.4vw'}),
            'due_date':forms.DateInput(attrs={'type': 'date'}),
   

        }

class loginForm(forms.Form):
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'name','placeholder':'Enter username'}))
    pwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'pwd'}))
        

class signupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    class Meta:
        model=User
        fields=['username','email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =["profile_pic",]

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]

