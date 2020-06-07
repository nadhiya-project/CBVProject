from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from basic_app.models import School,Student
# Create your views here.
"""
class IndexView(View):
    def get(self,request):
        return HttpResponse("HAI CBV IS SO SIMPLE")
"""
class IndexView(TemplateView):
    template_name="index.html"
"""
class HomeView(TemplateView):
    template_name="home.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']="THIS IS AN INJECTED DATA USING CBV"
        return context
"""
class SchoolListView(ListView):
    context_object_name='schools'
    model=School
class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=School
    template_name='basic_app/schooldetail_views.html'
