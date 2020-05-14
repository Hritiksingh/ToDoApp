from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views import generic
from .models import DailyWorks
from .forms import *


class IndexView(generic.ListView):
    template_name = 'Todo/index.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        return DailyWorks.objects.all()


class DailyWorksCreate(CreateView):
    model = DailyWorks
    form_class = DailyWorksForm
