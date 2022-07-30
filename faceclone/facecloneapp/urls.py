from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("home/",views.home,name = 'home'),
    path("profile",views.profile,name = 'profile'),
    path('logout',views.log_out,name='log_out'),
    
]