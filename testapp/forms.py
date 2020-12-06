from django import forms
from testapp.models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeModel
        fields="__all__"
