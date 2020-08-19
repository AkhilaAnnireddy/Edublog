from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Student,Faculty

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.phone_number=self.cleaned_data.get('phone_number')
        student.location=self.cleaned_data.get('location')
        student.save()
        return user

class FacultySignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_faculty = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        faculty = Faculty.objects.create(user=user)
        faculty.phone_number=self.cleaned_data.get('phone_number')
        faculty.designation=self.cleaned_data.get('designation')
        faculty.save()
        return user
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['phone_number','designation','contact_facebook','contact_linkedin','image']