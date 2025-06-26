from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm,\
    PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UsersRegisterForm, UsersProfileForm, UsersPasswordChangeForm

from .forms import UsersLoginForm
from django.contrib.auth import get_user_model


# Create your views here.

class UsersLogin(LoginView):
    form_class = UsersLoginForm
    template_name = 'users/login.html'
    next_page = ''
    extra_context = {'title': "Sign in",
                     'button_name': 'Sign in'}


class UsersLogout(LoginRequiredMixin, LogoutView):
    next_page = 'users:login'


class UsersRegister(SuccessMessageMixin, CreateView):
    form_class = UsersRegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': "Create account",
                     'button_name': 'Sign up'}
    success_url = reverse_lazy('users:login')


class UsersProfile(LoginRequiredMixin, UpdateView):
    form_class = UsersProfileForm
    template_name = 'users/profile.html'
    model = get_user_model()
    extra_context = {'title': "Profile",
                     'button_name': 'Save info'}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UsersPasswordChange(LoginRequiredMixin,PasswordChangeView):
    form_class = UsersPasswordChangeForm
    success_url = reverse_lazy("users:password-change-done")
    template_name = 'users/password_change.html'
    extra_context = {'title': "Changing password",
                     'button_name': 'Change password'}


class UsersPasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'

