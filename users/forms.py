from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = (
			'username',
		)

	def save(self, commit=True):
		user = super(CustomUserCreationForm, self).save(commit=False)
		user.username = self.cleaned_data['username']

		if commit:
			user.save()

		return user

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
