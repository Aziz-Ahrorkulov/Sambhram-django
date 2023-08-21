from django import forms
from .models import JobApplication, Gender
from phonenumber_field.formfields import PhoneNumberField

class JobApplicationForm(forms.ModelForm):

    first_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'id': 'firstName', 'class': 'form-control form-control-lg', 'type' : 'text'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'id': 'lastName', 'class': 'form-control form-control-lg', 'type' : 'text'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'id':' emailAddress', 'class': 'form-control form-control-lg', 'type' : 'email'}))
    phone = PhoneNumberField(label='Phone', widget=forms.NumberInput(attrs={'id':' phoneNumber', 'class': 'form-control form-control-lg', 'type' : 'tel'}))
    resume = forms.FileField(label='File', widget=forms.FileInput(attrs={'type': 'file', 'name': 'resume', 'accept' : '.pdf,.doc,.docx', 'id' : 'resume'}))
    birtday = forms.DateField(label='Date', widget=forms.DateInput(attrs={'id': 'birthdayDate', 'type': 'date', 'class': 'form-control form-control-lg',}))
    gender = forms.ChoiceField(choices=Gender.choices, widget=forms.RadioSelect(attrs={'class' : 'form-check-input', 'name' : 'inlineRadioOptions', 'type' : 'radio'}))



    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone', 'birtday', 'resume', 'gender']