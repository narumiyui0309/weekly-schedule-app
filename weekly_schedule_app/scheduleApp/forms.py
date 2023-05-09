from django import forms
from django.utils import timezone

class EditSchedule(forms.Form):
    schedule = forms.CharField(label="スケジュール",max_length=255)
    startDate = forms.DateField(label="開始日")
    endDate = forms.DateField(label="期限")