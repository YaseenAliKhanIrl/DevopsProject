from django import forms
from .models import BookingForm
 
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = ['full_name', 'student_no', 'date', 'time']