from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Projects
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    try:
        projects=Projects.objects.all()
    except Exception as e:
        raise  Http404()
    return render(request,'index.html',{"projects":projects})

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

def project_detail(request,project_id):
    try:
        projects=Projects.objects.filter(id=project_id)
    except Exception as e:
        raise Http404()

    return render(request,'details.html',{'projects':projects})
