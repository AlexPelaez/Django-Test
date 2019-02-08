from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm, EditProfileForm, EditPasswordForm
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# View to show the register form
# @todo Make more in depth register prossess 
# @param request 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


# View to show profile. When primary key is passed client is 
# able to view the profile assosiated with it. 
# @todo Make seperate views for personal and freinds
# @todo Upgrade UI design
# @param request 
# @param pk : Primary key assosiated to another User object
@login_required
def view_profile(request, pk = None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)
    

# View for users to edit there profile.
# @todo Make a nice UI and add more feautures
# @todo Add pictures
# @param request 
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('/account/profile')
    else:
        form= EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


# View for users to change there password.
# @param request         
@login_required
def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form= EditPasswordForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
