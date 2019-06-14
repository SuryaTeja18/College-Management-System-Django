from onlineApp.views.auth import *
from onlineApp.views import student,college
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class MockTest1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('problem1','problem2','problem3','problem4')

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('name','location','acronym','contact')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('name','email','db_folder','college_id')
        #fields = '__all__'\


class StudentDetailsSerializer(serializers.ModelSerializer):
    mocktest1 = MockTest1Serializer(read_only=True, many=False)

    model = Student
    fields = ('name','email','db_folder','college_id','mocktest1')

    def create(self, validated_data):
        newMarksRecord = validated_data.pop('mocktest1')
        newStudent = Student.objects.create(**validated_data)
        newMarksRecord['student'] = newStudent
        MockTest1.objects.create(**newMarksRecord)
        return newStudent
