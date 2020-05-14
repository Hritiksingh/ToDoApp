from django.db import models
from django.urls import reverse
from datetime import datetime
class DailyWorks(models.Model):
     goal = models.CharField(max_length=200)
     date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
     completed = models.BooleanField(default=False)

     def get_absolute_url(self):
          return reverse('Todo:index', kwargs={'pk':self.pk})

     def __str__(self):
          return self.goal+" - "+self.date



