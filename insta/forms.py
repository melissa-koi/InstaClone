from django import forms
from .models import Profile, Image, Post
from django.contrib.auth.models import User


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

# class UserRegisterForm(UserCreationForm):
#     '''
#     Adds more fields to user creation form
#     '''
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']