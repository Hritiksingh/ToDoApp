from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views import generic
from .models import DailyWorks

class IndexView(generic.ListView):
    template_name = 'Todo/index.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        return DailyWorks.objects.all()

