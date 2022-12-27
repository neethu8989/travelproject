from django.shortcuts import render
from .models import Studend, Studend1


def demo(request):
    obj = Studend.objects.all()
    obj1 = Studend1.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})
