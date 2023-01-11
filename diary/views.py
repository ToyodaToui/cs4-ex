from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

from django.views.generic import CreateView
from .forms import DiaryForm
from django.urls import reverse_lazy
class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')   

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

from django.views.generic import ListView
from .models import Diary
class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary
 
from django.views.generic import DetailView   
class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = Diary
   
from django.views.generic import UpdateView   
class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.updated_at = timezone.now()
        diary.save()
        return super().form_valid(form)
    
from django.views.generic import DeleteView  
class DiaryDeleteView(DeleteView):
    template_name = 'diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')