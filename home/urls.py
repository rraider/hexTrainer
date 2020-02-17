from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.start_view, name='start')
]