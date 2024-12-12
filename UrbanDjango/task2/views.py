from django.shortcuts import render
from django.views.generic import TemplateView


# Create your view here
def index(request):
    return render(request, 'class_template.html')


class index2(TemplateView):
    template_name = 'func_template.html'



