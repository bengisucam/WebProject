from django.forms import ModelForm
from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


YEARS = [x for x in range(1950, 2021)]
GENDERS = (
    ('FEMALE', 'female'),
    ('MALE', 'male')
)
ROLES = (
    ('CUSTOMER', 'customer')
)


class SignupForm(ModelForm):
    # gender = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDERS)
    gender = forms.CharField(widget=forms.Select(choices=GENDERS))
    password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}))

    class Meta:
        model = User
        # fields = ["first_name", "last_name", "date_of_birth", "email", "password", "gender", "role"]
        exclude = ('role', 'sport_center_id', 'address_id')







