from onlineApp.models import College
from django import forms

class AddCollegeForm(forms.ModelForm):
    class Meta:
        model = College
        exclude =['id']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': "Enter College Name",'class':'input is-primary' }),
            'acronym':forms.TextInput(attrs={'placeholder': "Enter College Acronym",'class':'input is-primary'}),
            'location':forms.TextInput(attrs={'placeholder':"Enter College Location",'class':'input is-primary'}),
            'contact':forms.EmailInput(attrs={'placeholder':"Enter Contact email",'class':'input is-primary'})
        }