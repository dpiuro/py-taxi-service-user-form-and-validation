from django import forms
from .models import Driver, Car


class LicenseNumberValidatorMixin:
    def validate_license_number(self, license_number):
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


class DriverLicenseUpdateForm(forms.ModelForm, LicenseNumberValidatorMixin):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        return self.validate_license_number(license_number)


class DriverCreationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["username", "license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        return self.validate_license_number(license_number)
