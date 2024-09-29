from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.password_validation import validate_password
from django.forms import (
    ModelForm,
    CheckboxSelectMultiple,
    ModelMultipleChoiceField
)

from taxi.models import Driver, Car


class DriverCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        validators=[validate_password]
    )
    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Driver
        fields = ["username", "license_number"]
        field_classes = {"username": UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Passwords do not match.")
        return cleaned_data


class CarCreationForm(ModelForm):
    drivers = ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]
