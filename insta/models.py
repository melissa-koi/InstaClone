from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    """
    Profile model

    Proxy Model that extends the base data with other information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('photos',default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return username"""
        return self.user.username

    @classmethod
    def get_user(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile

class Post(models.Model):
    """Post Model."""

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = CloudinaryField('photos')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.title, self.profile.user.username)

class Image(models.Model):
    '''
    Image model
    '''
    image = CloudinaryField('photos')
    image_name = models.CharField(max_length=30, blank=True)
    image_caption = models.TextField(max_length=100, blank=True)
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.image_caption

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_user(cls,username):
        images = cls.objects.filter(user__username__contains=username)
        return images