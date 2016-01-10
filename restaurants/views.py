# from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext
from restaurants.models import Restaurant, Food, Comment
from restaurants.forms import CommentForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
"""
def menu(request):
	path = request.path	
	restaurants = Restaurant.objects.all()
	r = Restaurant.objects.get(id=1)
	return render_to_response('menu.html', locals())
"""

def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	print request.user.user_permissions.all()
	return render_to_response('restaurants_list.html', RequestContext(request, locals()))

def menu(request, id):
	if id:
		r = Restaurant.objects.get(id=id)
		return render_to_response('menu.html', locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")

@permission_required('restaurants.can_comment', login_url='/accounts/login/')
def comment(request, id):	
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect("/restaurants_list/")
	# error = True
	# errors = []
	if request.POST:
		f = CommentForm(request.POST)
		if f.is_valid():
			visitor = f.cleaned_data['visitor']
			content = f.cleaned_data['content']
			email = f.cleaned_data['email']
			date_time = timezone.localtime(timezone.now())
			c = Comment.objects.create(
				visitor=visitor,
				email=email,
				content=content,
				date_time=date_time,
				restaurant=r
			)
			f = CommentForm()
	else:
		f = CommentForm();
	return render_to_response('comments.html', RequestContext(request, locals()))	
	
def meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))	
	
