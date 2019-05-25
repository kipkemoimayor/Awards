from django.shortcuts import render,redirect
from .forms import PostForm,RateForm
from .models import Projects,Rates
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
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

    if request.method=='POST':
        form=RateForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=request.user
            rate.project=project_id
            rate.save()
            return redirect('details',project_id)
    else:
        form=RateForm()

    #logic

    votes=Rates.objects.filter(project=project_id)
    usability=[]
    design=[]
    content=[]

    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content)

    average_usa=round(sum(usability)/len(usability),1)
    average_des=round(sum(design)/len(design),1)
    average_con=round(sum(content)/len(content),1)

    averageRating=round((average_con+average_des+average_usa)/3,1)


    return render(request,'details.html',{'projects':projects,'form':form,'usability':average_usa,'design':average_des,'content':average_con,'average':averageRating})

# def ajaxRequest(request,project_id):
#     if request.method=='POST':
#         form=RateForm(request.POST)
#         if form.is_valid():
#             rate=form.save(commit=False)
#             rate.user=request.user
#             rate.project=project_id
#             rate.save()
#             data={'success':'Your ratings have been recorded successfully '}
#             return JsonResponse(data)
