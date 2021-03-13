from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = 'Phone Number'

    class Meta:
        model = User
        fields = ('phone_number', 'password1', 'password2', )
        widgets = {
            'phone_number': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter phone number'}),
            'password1': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter Password'}),
        }


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=254, help_text='Required. Inform a valid phone number.',
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', "placeholder": "Phone Number"})
                             ) 
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', "class": "form-control", "placeholder": "Password"}),
    )
