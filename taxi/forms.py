from symtable import Class

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class DriverCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "license_number"
        ]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of exactly 8 characters."
            )
        if not (
                license_number[:3].isalpha() and license_number[:3].isupper()
        ):
            raise forms.ValidationError(
                "The first 3 characters must be uppercase letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError(
                "The last 5 characters must be digits."
            )
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of exactly 8 characters."
            )
        if not (
                license_number[:3].isalpha() and license_number[:3].isupper()
        ):
            raise forms.ValidationError(
                "The first 3 characters must be uppercase letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError(
                "The last 5 characters must be digits."
            )
        return license_number
