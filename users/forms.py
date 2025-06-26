from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import AuthenticationForm


class UsersLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Login')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Password')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UsersRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Login')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}),
                                label='Сonfirm the password')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name':  forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError("A user with such an email address has already been registered!")
            return email


class UsersProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}), label='Login')
    email = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}), label='E-mail')
    calc_count = forms.IntegerField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}),
                                    label='Calculations')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'calc_count']
        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
        }


class UsersPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['password1', 'password2']
        labels = {
            'email': 'E-mail',
            'password1': 'New password',
            'password2': 'Confirm the password',
        }

