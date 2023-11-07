from django.shortcuts import render
from .models import Casestudy1
from .models import Services
# Create your views here.
def index(request):
    obj = Casestudy1.objects.all()
    obj2 = Services.objects.all()
    return render(request, 'index.html', {'result': obj, 'result2': obj2})