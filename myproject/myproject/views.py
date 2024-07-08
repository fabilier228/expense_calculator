from django.http import HttpResponse
from django.shortcuts import render


def welcomepage(request):
    return render(request, 'welcome.html')