from django import forms
from .models import Profile, Image, Post
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    biography = forms.CharField(widget=forms.TextInput(), max_length=260, required=False)

    class Meta:
        model = Profile
        fields = ('picture', 'first_name', 'last_name', 'biography')

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