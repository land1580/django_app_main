from django.conf.urls import url
from . import views # from current directory (dot), import views.py file
urlpatterns = [
    url(r'^$', views.index), # Main route
    url(r'^new/', views.new), # "New" route
    url(r'^create/', views.create), # "Create" route
    url(r'(?P<number>[0-9]\d+)/$', views.show), # "Show" route matches any numbered request
    url(r'(?P<number>[0-9]\d+)/edit/$', views.edit), # "Edit" route matches any numbered request
    url(r'(?P<number>[0-9]\d+)/delete/$', views.destroy), # "Delete/Destroy" route matches any numbered request
]  