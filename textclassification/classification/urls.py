from django.urls import path

from . import views

app_name = 'classification'
urlpatterns = [
    path('',views.index, name='index'),
    path('ajax_posting', views.ajax_posting, name='ajax-posting')
]