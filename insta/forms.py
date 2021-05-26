from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UploadImage(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_caption']

class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile picture
    '''

    class Meta:
        model = Profile
        fields = ['biography','picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['created', 'user']
