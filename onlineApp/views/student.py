from onlineApp.models import *
from django.shortcuts import render,redirect
from django.views import View
from django.urls import resolve
import MySQLdb
from onlineApp.Forms.Student import *
from django.contrib.auth.mixins import LoginRequiredMixin

#imports related to restify the students CRUD API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from onlineApp.mySerializers import *

class AddStudent(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        form1 = AddStudentForm()
        form2 = MockMarksForm()
        return render(request,"addStudent.html",{"form1":form1,"form2":form2})

    def post(self,request,*args,**kwargs):
        form1 = AddStudentForm(request.POST)
        form2 = MockMarksForm(request.POST)
        if(form1.is_valid() and form2.is_valid()):
            temp1 = form1.save(commit=False)
            temp1.college = College.objects.get(**kwargs)
            temp1.save()
            temp2 = form2.save(commit=False)
            temp2.total = temp2.problem1 + temp2.problem2 + temp2.problem3 + temp2.problem4
            temp2.student = temp1
            temp2.save()
            college = College.objects.get(pk=kwargs['id']).name
            students = Student.objects.filter(college_id=kwargs['id'])
            return render(request, "showCollegeDetails.html", {'college':college,'students': students,'id':kwargs['id']})

class EditDeleteStudent(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if (resolve(request.path_info).url_name == 'edit_student'):
            student = Student.objects.get(**kwargs)
            marks=MockTest1.objects.get(student_id=kwargs.get('id'))
            form1 = AddStudentForm(instance=student)
            form2 = MockMarksForm(instance=marks)
            return render(request, "addStudent.html", {"form1": form1,"form2":form2,"op":"Edit Student "})
        elif(resolve(request.path_info).url_name == 'delete_student'):
            student = Student.objects.get(**kwargs)
            cid = student.college_id
            cname = student.college
            Student.objects.get(**kwargs).delete()
            students = Student.objects.filter(college_id=cid)
            #return render(request,"showCollegeDetails.html",{'college':cname,'student':students,'id':cid})
            #return redirect('{%url \'college/{{cid}}/\' %}')
            return render(request,"showAllColleges.html",{'colleges':College.objects.all()})
    def post(self,request,*args,**kwargs):
        if(resolve(request.path_info).url_name == 'edit_student'):
            student = Student.objects.get(**kwargs)
            marks = MockTest1.objects.get(student_id=kwargs.get('id'))
            cid = student.college_id
            form1 = AddStudentForm(request.POST,instance=student)
            form2 = MockMarksForm(request.POST,instance=marks)
            if (form1.is_valid() and form2.is_valid()):
                temp1 = form1.save(commit=False)
                temp1.college = College.objects.get(pk=cid)
                temp1.save()
                temp2 = form2.save(commit=False)
                temp2.total = temp2.problem1 + temp2.problem2 + temp2.problem3 + temp2.problem4
                temp2.student = temp1
                temp2.save()
                college = College.objects.get(pk=cid).name
                students = Student.objects.filter(college_id=cid)
                return render(request, "showCollegeDetails.html",{'college': college, 'students': students, 'id': kwargs.get('id')})


class students(APIView):
    def get(self,request,format=None,*args,**kwargs):
        if(kwargs):
            s = Student.objects.get(**kwargs)
            res = StudentSerializer(s)
            return Response(res.data)
        else:
            s = Student.objects.all()
            res = StudentSerializer(s,many=True)
            return Response(res.data)

    def post(self,request,format=None,*args,**kwargs):
        serializer = MockTest1Serializer(data=request.data)
        if serializer.is_valid():
            newStudentRecord = serializer.pop('student')
            studentSer = StudentSerializer(data=newStudentRecord.data)
            studentSer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)