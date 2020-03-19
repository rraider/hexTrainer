from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.http import request, HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import logout, login
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse

from .models import CustomUser as User

# Create your views here.

def log_out(request):
	logout(request)
	return render(request, 'registration/logged_out.html')

def sign_up(request):
	if request.POST:
		form = CustomUserCreationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			#messages.success(request, "Succesfully Registered", extra_tags="green")
			return HttpResponseRedirect(reverse('users:profile_detail_view', kwargs={'user_id': request.user.id}))

	else:
		form = CustomUserCreationForm()

	args = {'form': form}
	return render(request, 'registration/reg_form.html', args)

@login_required
def profile_detail_view(request, user_id):
	user = User.objects.get(id=user_id)
	template_name = 'profiles/profile_detail_view.html'

	return render(request, template_name, {
		"other_user": user
	})

@login_required
def profile(request):
	return render(request, 'profiles/profile_detail_view.html', {"other_user": request.user})

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()

		return HttpResponseRedirect(reverse('users:profile_detail_view', kwargs={"user_id": request.user.id}))
	else:
		form = CustomUserChangeForm(instance=request.user)

	args = {'form': form}
	return render(request, 'profiles/edit_profile.html', args)

def password_change_done(request):
	return HttpResponseRedirect(reverse('users:profile_detail_view', kwargs={'user_id': request.user.id}))

def change_password(request):
	if request.method == 'POST':
		_user = request.user
		print(_user)
		form = PasswordChangeForm(request.POST, user=_user)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:profile_detail_view', kwargs={"user_id": request.user.id}))

	else:
		form = PasswordChangeForm(user=request.user)
	args = {'form': form}
	return render(request, 'registration/password_change.html', args) # war vorher 'profiles/change_password.html'


@login_required
def add_xp(request):
	xp = request.GET.get('xp')

	request.user.xp += int(xp)
	request.user.save()

	return JsonResponse({"success": True})