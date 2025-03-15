from django.db import models

# Create your models here.

 
class register_table(models.Model):
    username = models.CharField(max_length=100)
    student_ID = models.CharField(max_length=100)  # Ensure the correct field name
    password = models.CharField(max_length=100)
