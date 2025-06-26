from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
