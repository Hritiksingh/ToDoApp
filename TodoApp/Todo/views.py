from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from .models import DailyWorks
from .forms import DailyWorksForm
from django.shortcuts import render,get_object_or_404











class IndexView(generic.ListView):
    template_name = 'Todo/index.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        return DailyWorks.objects.all()


class DailyWorksCreate(CreateView):
    model = DailyWorks
    form_class = DailyWorksForm



def delete_dailyworks(request, work_id):
    item = DailyWorks.objects.get(id=work_id)
    item.delete()
    items = DailyWorks.objects.filter()
    return render(request, 'Todo/index.html', {'all_tasks': items})

