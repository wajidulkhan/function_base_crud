from django.forms import ModelForm, forms, widgets
from django.shortcuts import render
from .models import user
from django import forms

# Create the form class.
class studentForm(ModelForm):
     class Meta:
        model = user
        fields = ['id', 'name', 'email', 'password'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'},render_value=True), 
          } 
        error_messages = {
            'name': {
                'required': "Please enter your name", 
            }
        }