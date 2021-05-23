from django.shortcuts import render, redirect
from .models import Post, Profile, Image
import datetime as dt
from django.contrib import messages
from .forms import ProfileUpdateForm,UserUpdateForm

# Create your views here.
def home(request):
    title="title"
    return render(request, 'index.html',{"title": title})


def profile(request):
    '''
    This method handles the user profile
    '''
    title = 'Profile'
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"You Have Successfully Updated Your Profile!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'title':title,
            'u_form':u_form,
            'p_form':p_form
        }
    return render(request,'profile.html',context)