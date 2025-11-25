from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'location',
            'salary_from',
            'salary_to',
            'employment_type',
            'schedule',
            'experience_level',
            'requirements',
            'responsibilities',
            'languages',
        ]
        labels = {
            'title': 'Название вакансии',
            'description': 'Описание вакансии',
            'location': 'Локация (город)',
            'salary_from': 'Зарплата от',
            'salary_to': 'Зарплата до',
            'employment_type': 'Тип занятости',
            'schedule': 'Формат работы',
            'experience_level': 'Требуемый опыт',
            'requirements': 'Требования',
            'responsibilities': 'Обязанности',
            'languages': 'Знание языков (через запятую)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 3}),
            'responsibilities': forms.Textarea(attrs={'rows': 3}),
        }
