from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


# This is the form that users create an account with
# @param UserCreationForm : This is the generic django template for user registration.
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
        )

def save(self, commit=True):
    user = super(RegistrationForm, self).save(commit=False)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.email = self.cleaned_data['email']

    if commit:
        user.save()

# This is the form that users edit there name, email. 
# This form links to the edit password page.
# @param UserChangeForm : This is the generic django template for editing the User object.
class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
        'first_name',
        'last_name',
        'email',
        )

# This is the form that users create an account with
# @param PasswordChangeForm : This is the generic django template for user registration.
class EditPasswordForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = (
        'old_password',
        'new_password1',
        'new_password2',
        )
