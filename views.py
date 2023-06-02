from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .en_forms import EnSignUpForm, EnEditProfileForm
from .es_forms import EsSignUpForm, EsEditProfileForm

# Create your views here.
def es_home(request):
    return render(request, 'authenticate/es/home.html', {})

def en_home(request):
    return render(request, 'authenticate/en/home.html', {})

def es_login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('"¡Has iniciado sesión!"'))
			return redirect('es_home')

		else:
			messages.success(request, ('Error al iniciar sesión. Por favor, inténtalo de nuevo...'))
			return redirect('es_login')
	else:
		return render(request, 'authenticate/es/login.html', {})

def en_login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You Have Been Logged In!'))
			return redirect('en_home')

		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('en_login')
	else:
		return render(request, 'authenticate/en/login.html', {})

def es_logout_user(request):
	logout(request)
	messages.success(request, ('Has cerrado sesión...'))
	return redirect('es_home')

def en_logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('en_home')

def es_register_user(request):
	if request.method == 'POST':
		form = EsSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Te has registrado..'))
			return redirect('es_home')
	else:
		form = EsSignUpForm()
	
	context = {'form': form}
	return render(request, 'authenticate/es/register.html', context)

def en_register_user(request):
	if request.method == 'POST':
		form = EnSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('You Have Registered...'))
			return redirect('en_home')
	else:
		form = EnSignUpForm()
	
	context = {'form': form}
	return render(request, 'authenticate/en/register.html', context)

def es_edit_profile(request):
	if request.method == 'POST':
		form = EsEditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Has editado tu perfil...'))
			return redirect('es_home')
	else:
		form = EsEditProfileForm(instance=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/es/edit_profile.html', context)

def en_edit_profile(request):
	if request.method == 'POST':
		form = EnEditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Profile...'))
			return redirect('en_home')
	else:
		form = EnEditProfileForm(instance=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/en/edit_profile.html', context)

def es_change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('Has editado tu contraseña...'))
			return redirect('es_home')
	else:
		form = PasswordChangeForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/es/change_password.html', context)

def en_change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('en_home')
	else:
		form = PasswordChangeForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/en/change_password.html', context)
