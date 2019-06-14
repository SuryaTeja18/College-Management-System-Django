from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from onlineApp.models import *
from django.shortcuts import render,redirect
from django.views import View
from django.urls import resolve
from onlineApp.Forms.colleges import *
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, serializers
#from onlineApp.mySerializers import StudentSerializer,CollegeSerializer

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('name','location','acronym','contact')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('name','email','db_folder','college_id')

class ShowAllColleges(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        permissions = request.user.get_all_permissions()
        if(not kwargs):
            colleges = College.objects.all()
            return render(request,"showAllColleges.html",{'colleges':colleges,"permissions":permissions})
        else:
            college = College.objects.get(pk=kwargs['id']).name
            students = Student.objects.filter(college_id=kwargs['id'])
            return render(request, "showCollegeDetails.html", {'college':college,'students': students,'id':kwargs.get('id'),"permissions":permissions})
            # students = MockTest1.objects.values("total","student__dob","student__email","student__db_folder","student__name","MockTest1__Student__total").filter(college_id=kwargs['id'])
            # return render(request, "showCollegeDetails.html", {'college':college,'students': students,'id':kwargs.get('id')})

class AddCollege(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if (resolve(request.path_info).url_name == 'delete_college'):
            College.objects.get(**kwargs).delete()
            return redirect("colleges")
        if (resolve(request.path_info).url_name == 'edit_college'):
            college = College.objects.get(**kwargs)
            form = AddCollegeForm(instance=college)
            return render(request, "addCollege.html", {"form": form,"op":"Edit College"})
        form = AddCollegeForm()
        return render(request,"addCollege.html",{"form":form,"op":"Add College"})

    def post(self,request,*args,**kwargs):
        if(resolve(request.path_info).url_name=='edit_college'):
            college = College.objects.get(**kwargs)
            form = AddCollegeForm(request.POST,instance = college)
            if(form.is_valid()):
                form.save()
            return redirect('colleges')
        form = AddCollegeForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('colleges')


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def colleges(request,*args,**kwargs):
    if request.method == 'GET':
        if(kwargs):
            cid = College.objects.get(**kwargs).id
            res = StudentSerializer(Student.objects.filter(college_id = cid),many=True)
            return Response(res.data)
        else:
            res = CollegeSerializer(College.objects.all(),many=True)
            return Response(res.data)
    if request.method == "POST":
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        college = College.objects.get(**kwargs)
        serializer = CollegeSerializer(college,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        college = College.objects.get(**kwargs)
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def test_view(request):
    return HttpResponse('test-response')