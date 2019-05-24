from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def post(request):
    current_user=request.user
    if request.method=='POST':
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
        return redirect("index")
    else:
        form=PostForm()
    return render(request,'post.html',{'form':form})
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'profile.html' )
