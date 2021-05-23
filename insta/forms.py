from django import forms
from .models import Profile
class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    biography = forms.CharField(widget=forms.TextInput(), max_length=260, required=False)

    class Meta:
        model = Profile
        fields = ('picture', 'first_name', 'last_name', 'biography')
