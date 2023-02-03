from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),   
            'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fathers Name'}),
            'fathers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fathers Number'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mothers Name'}),
            'mothers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mothers Number'}),
        }

