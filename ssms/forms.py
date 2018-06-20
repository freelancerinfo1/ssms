# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import ContactUs
class ContactUsForm(ModelForm):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Name'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Subject'}))
	message = forms.CharField(label="message",required=True,max_length=500,widget=forms.Textarea(attrs={"rows":3,'placeholder':'Message'}))
	class Meta:
		model = ContactUs
		fields = "__all__"
