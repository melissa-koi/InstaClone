from django.shortcuts import render, redirect
from .models import Profile, Image, Comment, Likes
import datetime as dt
from django.contrib import messages
from .forms import ProfileUpdateForm,UserUpdateForm, UploadImage, CommentForm

# Create your views here.
def home(request):
    title="explore page"
    images = Image.get_all()
    form = CommentForm()
    comments = Comment.objects.all()
    all_likes = Likes.objects.all()
    return render(request, 'index.html',{"title": title, "posts":images, "form":form, "comments":comments, "likes":all_likes})

def image_detail(request, username):
    images = Image.get_image_by_user(username)
    form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'image_detail.html',{"posts":images, "form":form, "comments":comments})

def comment(request,pk):
    image=Image.objects.get(pk=pk)
    comments=request.GET.get("comments")
    current_user=request.user
    comment = Comment(image=image,comment=comments,user=current_user)
    comment.save_comment()

    return redirect('home')


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
            #return redirect('profile/1')
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
        return redirect('home')
    else:
        form = UploadImage()
    return render(request, 'post_image.html', {"form":form})

def Like(request,pk):
    '''
    Implements the like functionality in the app
    '''
    current_user = request.user
    likes = Likes.objects.filter(user=current_user).first()
    if likes is None:
        image = Image.objects.get(pk=pk)
        current_user = request.user
        user_likes = Likes(user=current_user,image=image)
        user_likes.save()
        return redirect('home')
    else:
        likes.delete()
        return redirect('home')

def search_results(request):
    model=Image