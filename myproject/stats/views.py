from django.shortcuts import render

# Create your views here.

def stat_page(request):
    return render(request, 'stats/main.html', {'stats': 'Your statistics data'})