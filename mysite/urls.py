from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
"""
from views import here, math
from views import login, logout
"""
from views import index, welcome, register
from restaurants.views import menu, meta, list_restaurants, comment, foodcomment
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
	
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^here/$', here),
	# url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
	
    url(r'^admin/', include(admin.site.urls)),	
	url(r'^accounts/login/$', login, {'template_name':'login.html'}),
	url(r'^accounts/logout/$', logout, {'template_name':'logout.html'}),	
	url(r'^accounts/register/$', register),
	url(r'^index/$', index),
	url(r'^menu/(\d{1,5})/$', login_required(menu)),
	url(r'^restaurants_list/$', list_restaurants),
	url(r'^comment/(\d{1,5})/$', login_required(comment)),	
	url(r'^foodcomment/(\d{1,5})/$', login_required(foodcomment)),		
	
	url(r'^welcome/$', welcome),	
	url(r'^meta/$', meta),
)
