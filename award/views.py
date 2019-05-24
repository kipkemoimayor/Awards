from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,'index.html')


def post(request):
    form=PostForm()
    return render(request,'post.html',{'form':form})

def profile(request):
    return render(request,'profile.html' )
