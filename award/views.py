from django.shortcuts import render,redirect
from .forms import PostForm,RateForm,ReviewForm,UpdateForm
from .models import Projects,Rates,Comments,Profile
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer

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
    current_user=request.user
    try:
        profis=Profile.objects.filter(user=current_user)[0:1]
        user_projects=Projects.objects.filter(user=current_user)
    except Exception as e:
        raise  Http404()
    if request.method=='POST':
        form=UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
        return redirect('profile')
    else:
        form=UpdateForm()
    return render(request,'profile.html', {'form':form,'profile':profis,'projects':user_projects})

def project_detail(request,project_id):
    try:
        projects=Projects.objects.filter(id=project_id)
        all=Rates.objects.filter(project=project_id)
    except Exception as e:
        raise Http404()
    #user single
    count=0
    for i in all:
        count+=i.usability
        count+=i.design
        count+=i.content

    if count>0:
        ave=round(count/3,1)
    else:
        ave=0


    if request.method=='POST':
        form=RateForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=request.user
            rate.project=project_id
            #review
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
    if len(usability) > 0 or len(design)> 0 or len(content) >0:

        average_usa=round(sum(usability)/len(usability),1)
        average_des=round(sum(design)/len(design),1)
        average_con=round(sum(content)/len(content),1)

        averageRating=round((average_con+average_des+average_usa)/3,1)
    else:
        average_usa=0.0
        average_des=0.0
        average_con=0.0
        averageRating=0.0
    '''
    Restricting user to rate only once
    '''
    arr1=[]
    for use in votes:
        arr1.append(use.user_id)

    auth=arr1


    if request.method=='POST':
        review=ReviewForm(request.POST)
        if review.is_valid():
            comment=review.save(commit=False)
            comment.user=request.user
            comment.pro_id=project_id
            comment.save()
            return redirect('details',project_id)
    else:
        review=ReviewForm()

    try:
        user_comment=Comments.objects.filter(pro_id=project_id)
    except Exception as e:
        raise Http404()
    return render(request,'details.html',{'projects':projects,'form':form,'usability':average_usa,'design':average_des,'content':average_con,'average':averageRating,'auth':auth,'all':all,'ave':ave,'review':review,'comments':user_comment})

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

def search(request):

    if 'name' in request.GET and   request.GET['name']:
        term=request.GET.get('name')
        results=Projects.search_project(term)

        return render(request,'search.html',{'projects':results})
    else:
        message="You havent searched any project"
        return render(request,'search.html',{'message':message})

'''
API View
'''
class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects=Projects.objects.all()
        serializers=ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles=Profile.objects.all()
        serializers=ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)
@login_required(login_url='/accounts/login/')
def apiView(request):
    current_user=request.user
    title="Api"
    profis=Profile.objects.filter(user=current_user)[0:1]
    return render(request,'api.html',{"title":title,'profile':profis})
