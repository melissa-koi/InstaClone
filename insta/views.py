from django.shortcuts import render, redirect
from .models import Profile, Image, Comment, Likes
import datetime as dt
from django.contrib import messages
from .forms import ProfileUpdateForm, UserUpdateForm, UploadImage, CommentForm, RegisterForm, CreateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    title="explore page"
    images = Image.get_all()
    form = CommentForm()
    comments = Comment.objects.all()
    all_likes = Likes.objects.all()
    return render(request, 'index.html',{"title": title, "posts":images, "form":form, "comments":comments, "likes":all_likes})

@login_required(login_url='/login/')
def image_detail(request, username):
    images = Image.get_image_by_user(username)
    form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'image_detail.html',{"posts":images, "form":form, "comments":comments})

@login_required(login_url='/login/')
def comment(request,pk):
    image=Image.objects.get(pk=pk)
    comments=request.GET.get("comments")
    current_user=request.user
    comment = Comment(image=image,comment=comments,user=current_user)
    comment.save_comment()

    return redirect('home')

@login_required(login_url='/login/')
def profile(request, username):
    '''
    This method handles the user profile
    '''
    title = 'Profile'
    images = Image.get_image_by_user(username)
    profile = Profile.get_user(username)
    return render(request,'profile.html',{"title":title, "images": images, "profile":profile})

@login_required(login_url='/login/')
def create_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = CreateProfileForm()
    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.get_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'accounts/login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('home')

