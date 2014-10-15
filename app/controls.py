import os

from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from app import data, forms

# Create your views here.

def userBlock(request):
	return HttpResponseRedirect(reverse("app:home") )


def userContact(request):
	return HttpResponseRedirect(reverse("app:home") )


def userLogin(request):
	return HttpResponseRedirect(reverse("app:home") )


def userProfileUpdate(request):
	return HttpResponseRedirect(reverse("app:home") )


def userRegister(request):
	return HttpResponseRedirect(reverse("app:home") )


def userReview(request):
	return HttpResponseRedirect(reverse("app:home") )


def routeAdd(request):
	return HttpResponseRedirect(reverse("app:home") )


def routeRemove(request):
	return HttpResponseRedirect(reverse("app:home") )


def routeSearch(request):
	return HttpResponseRedirect(reverse("app:home") )


def routeUpdate(request):
	return HttpResponseRedirect(reverse("app:home") )


