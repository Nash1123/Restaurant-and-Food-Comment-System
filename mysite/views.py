# -*- coding: utf-8 -*-
"""
from django import template
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
"""
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext
from restaurants.models import Restaurant, Food, Comment
from restaurants.forms import CommentForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/accounts/login/')			
	else:
		form = UserCreationForm()
	return render_to_response('register.html', RequestContext(request, locals()))		

def index(request):
	return render_to_response('index.html', RequestContext(request, locals()))

def welcome(request):
	if 'user_name' in request.GET and request.GET['user_name'] != '':
		return HttpResponse('Welcome!~'+request.GET['user_name'])
	else:
		return render_to_response('welcome.html', locals())

def here(request):
	return HttpResponse('¶ý§Ú¦b³o!')

def math(request, a, b):
	a = int(a) 
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	"""
	with open('mysite/templates/math.html','r') as reader:
		t = template.Template(reader.read())
	c = template.Context({'s':s,'d':d,'p':p,'q':q})
	return HttpResponse(t.render(c))
	"""
	return render_to_response('math.html', locals())
	
"""
def menu(request):
	food1 = {'name':'Black Pepper Chicken', 'price':6.75, 'comment':'good', 'is_spicy':False}
	food2 = {'name':'Kung Po Chicken', 'price':6.75, 'comment':'good', 'is_spicy':True}
	foods = [food1, food2]
	return render_to_response('menu.html', locals())
	
def login(request):	
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')	
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')	
	user = auth.authenticate(username=username, password=password)	
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html', RequestContext(request, locals()))
	
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')
"""



