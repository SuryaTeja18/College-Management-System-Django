from django import forms
from onlineApp.models import Student,MockTest1

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude=['dob','college']
        widgets ={
            'name':forms.TextInput(attrs={'placeholder':'Enter Student name','class':'input is-success'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Student email','class':'input is-success'}),
            'db_folder':forms.TextInput(attrs={'placeholder':'Enter Student\'s db folder name','class':'input is-success'})
        }

class MockMarksForm(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['total','student']
        widgets = {
            'problem1': forms.NumberInput(attrs={'placeholder':'Enter p1 marks','class':'input is-success'}),
            'problem2': forms.NumberInput(attrs={'placeholder':'Enter p2 marks','class':'input is-success'}),
            'problem3': forms.NumberInput(attrs={'placeholder':'Enter p3 marks','class':'input is-success'}),
            'problem4': forms.NumberInput(attrs={'placeholder':'Enter p4 marks','class':'input is-success'}),
        }