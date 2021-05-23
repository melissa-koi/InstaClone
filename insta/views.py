from django.shortcuts import render
from .models import Post, Profile
# Create your views here.
def home(request):
    title="title"
    return render(request, 'index.html',{"title": title})

def my_profile(request, profile_id):
    date = dt.date.today()
    profile = Profile.objects.filter(id=profile_id)
    images = Image.objects.filter(user=request.user)
    return render(request, 'profile.html', {"date": date, "profile": profile, "images": images, })