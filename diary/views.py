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