from django.shortcuts import render, redirect
from .models import Profile, Image
import datetime as dt
from django.contrib import messages
from .forms import ProfileUpdateForm,UserUpdateForm, UploadImage

# Create your views here.
def home(request):
    title="title"
    images = Image.get_all()
    return render(request, 'index.html',{"title": title, "posts":images})

def profile(request, username):
    '''
    This method handles the user profile
    '''
    title = 'Profile'
    images = Image.get_image_by_user(username)
    profile = Profile.get_user(username)
    return render(request,'profile.html',{"title":title, "images": images, "profile":profile})

def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"You Have Successfully Updated Your Profile!")
            return redirect('profile/1')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request,'update_profile.html',{"u_form":u_form, "p_form":p_form})

def post_photo(request):
    C_user = request.user
    if request.method == "POST":
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = C_user
            img.save()
        # return redirect('index')
    else:
        form = UploadImage()
    return render(request, 'post_image.html', {"form":form})

def image_detail(request, pk):
    model = Image
