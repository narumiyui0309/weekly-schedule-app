from django.shortcuts import render
from django.views import generic
from .forms import EditSchedule

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class ScheduleDetailView(generic.FormView):
    template_name = "detail.html"
    form_class = EditSchedule
