from django.db import models

# Create your models here.
class BookingForm(models.Model):
    full_name = models.CharField(max_length=200)
    student_no = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    time = models.TimeField(max_length=100)
    
    def __str__(self):
        return f"{self.full_name}"+" "