from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/<username>', views.profile, name="profile"),
    path('profile/update/', views.update_profile, name="update_profile"),
    path('profile/post/', views.post_photo, name = 'post_photo'),
    path('comment/<pk>/', views.comment, name = 'AddComment'),
    path('image/detail/<username>', views.image_detail, name="image_detail"),
    path('like/<pk>/', views.Like, name="image-like"),
    path('search/', views.search_results, name = 'search_results'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('create_profile/',views.create_profile,name='create_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

