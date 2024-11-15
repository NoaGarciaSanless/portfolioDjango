from django.db import models
import datetime

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    
    # Lets the user pick the date
    #date = models.DateField(default=datetime.date.today)
    
    # Doesn't let the user pick the date
    date = models.DateField(auto_now_add=True)
    
    description = models.TextField(max_length=500)