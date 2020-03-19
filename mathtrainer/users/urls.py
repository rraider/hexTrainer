from django.urls import path
from django.conf.urls import url
from . import views, forms
from django.contrib.auth import views as auth_views

from django.views.generic.base import TemplateView

app_name = "users"
urlpatterns = [
	path('logout/', views.log_out, name='logout'),
	path('signup/', views.sign_up, name='signup'),
	path('profile/', views.profile, name='profile'),
	path('profile/<int:user_id>/details/', views.profile_detail_view, name="profile_detail_view"),
	path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/password/', auth_views.PasswordChangeView.as_view(), name='password'),
	path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('add_xp/', views.add_xp, name='add_xp')
]