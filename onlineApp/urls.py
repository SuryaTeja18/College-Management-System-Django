from django.urls import include, path  # For django versions from 2.0 and up
from onlineApp.views import *
from django.contrib import admin
#from django.conf.urls.defaults import *
from onlineApp.views.auth import *
from onlineApp.views import student,college
from onlineApp.mySerializers import *
from rest_framework.decorators import api_view
from onlineApp.authToken import *


urlpatterns = [
    path('colleges/',college.ShowAllColleges.as_view(),name="colleges"),
    path('colleges/<int:id>',college.ShowAllColleges.as_view(),name="collegeDetails"),
    path('college/add/',college.AddCollege.as_view(),name="addCollege"),
    path('college/edit/<int:id>',college.AddCollege.as_view(),name="edit_college"),
    path('college/delete/<int:id>',college.AddCollege.as_view(),name="delete_college"),

    path('student/add/<int:id>',student.AddStudent.as_view(),name="add_student"),
    path('student/edit/<int:id>',student.EditDeleteStudent.as_view(),name="edit_student"),
    path('student/delete/<int:id>',student.EditDeleteStudent.as_view(),name="delete_student"),

    path('login/',Login.as_view(),name="login"),
    path('signup/',SignUp.as_view(),name="signup"),
    path('logout/',logout_user,name="logout"),

path('api/v1/colleges/',college.colleges,name="api_colleges"),
    path('api/v1/colleges/<int:id>/',college.colleges,name="api_colleges_put_delete"),


    path('api/v1/students/<int:id>/',student.students.as_view(),name="api_students_crud"),
    path('api/v1/students/',student.students.as_view(),name="api_students_display"),

    path('test/',college.test_view,name="test-response"),
    path('getAuthToken/',getToken,name='get-token'),
]