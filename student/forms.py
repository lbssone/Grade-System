from django import forms
from django.forms import ModelForm

from .models import Student, Grade

class CUStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["firstName", "lastName", "phone"]
        labels = {
            "firstName": "First Name",
            "lastName": "Last Name",
            "phone": "Phone"
        }
        widgets = {
            "firstName": forms.TextInput(attrs={"class": "form-control"}),
            "lastName": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"})
        }


class CUGradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ["testNo", "chinese", "english", "math"]
        labels = {
            "testNo": "Test Number"
        }
        widgets = {
            "testNo": forms.NumberInput(attrs={"class": "form-control"}),
            "chinese": forms.NumberInput(attrs={"class": "form-control"}),
            "english": forms.NumberInput(attrs={"class": "form-control"}),
            "math": forms.NumberInput(attrs={"class": "form-control"}),
        }