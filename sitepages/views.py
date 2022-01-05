
from django.shortcuts import render

#DataFlair #Views #TemplateInheritance
# Create your views here.
def home(request):
    return render(request, 'base.html')

def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html')


from django.views.generic import CreateView
from .models import Person

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')
