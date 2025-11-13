from django import forms
from .models import Employer

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'position', 'profile_image', 'profile_video']
