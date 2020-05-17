from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils import timezone



class DailyWorks(models.Model):
     goal = models.CharField(max_length=200)
     date = models.DateField(auto_now_add=False, auto_now=False, blank=True, default=timezone.now())
     completed = models.BooleanField(default=False)

     def get_absolute_url(self):
          return reverse('Todo:index')

     def __repr__(self):
          return self.goal+" - "+str(self.date)



