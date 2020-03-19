from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	path('train/', views.start_view, name='train'),
	path('scoreboard/', views.scoreboard, name='scoreboard')
]