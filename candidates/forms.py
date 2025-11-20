from django import forms
from .models import CV, Skill


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['full_name', 'age', 'experience', 'education']

        labels = {
            'full_name': 'ФИО',
            'age': 'Возраст',
            'experience': 'Опыт работы',
            'education': 'Образование',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше полное имя'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш возраст'
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваш опыт работы',
                'rows': 3
            }),
            'education': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваше образование',
                'rows': 3
            }),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']

        labels = {
            'name': 'Навык',
            'level': 'Уровень',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Python, Django, Excel'
            }),
            'level': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
