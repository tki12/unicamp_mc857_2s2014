# !/usr/bin/python
# coding=utf-8

from django import forms

from app.models import Route

# Create your forms here

class UserLogin(forms.Form):
	pass


class UserRegister(forms.Form):
	pass


class UserUpdate(forms.Form):
	pass


class UserReview(forms.Form):
	pass


class RouteAdd(forms.Form):
	pass


class RouteUpdate(forms.Form):
	pass
	class Meta:
		model = Route
		excludes =['id']
