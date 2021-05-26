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


class Image(models.Model):
    '''
    Image model
    '''
    image = CloudinaryField('photos')
    image_name = models.CharField(max_length=30, blank=True)
    image_caption = models.TextField(max_length=100, blank=True)
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="img_user", on_delete=models.CASCADE, null=True)

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

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments", null=True)

    def save_comment(self):
        self.save()

    @classmethod
    def get_post_comments(cls,image):
        return cls.objects.filter(image=image)

class Followers(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

class Likes(models.Model):
    '''
    This model will contain the columns to our likes class
    '''
    image_like = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def __int__(self):
        return self.like