from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name = 'index'),
	url(r'^(\d+)/$',views.detail,name='detail'),
	url(r'^(\d+)/results/$',views.results,name='results'),
	url(r'^(\d+)/vote/$',views.vote,name='vote'),
	url(r'^confirm/$',views.confirm,name='confirm'),
]