from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse
from rest_framework.reverse import reverse


# Create your views here.

def employees(request):
    emp = reverse('emp')

    return HttpResponse('<h1>{}</h1>'.format(emp))
