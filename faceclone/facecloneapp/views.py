from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import UserProfile


# Create your views here.
def index(request): #request(current user , POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('index')
    else:
        if request.user.is_authenticated:
            return redirect('home')

        else:
            return render(request,'index.html')






def home(request):
    user = request.user
    pro = UserProfile.objects.get(user=user)
    context = {'username':user.username,'status': pro.status}
    return render(request,'home.html',context)
def profile(request):
    user = request.user
    pro = UserProfile.objects.get(user=user)
    context = {'username':user.username,'pro':pro}
    return render(request,'profile.html',context)



def log_out(request):
    logout(request)
    return redirect('index')
