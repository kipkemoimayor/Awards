from django.shortcuts import render
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def post(request):
    form=PostForm()
    return render(request,'post.html',{'form':form})
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'profile.html' )
