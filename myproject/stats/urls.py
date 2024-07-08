from django.urls import path
from . import views

app_name = 'stats'


urlpatterns = [
    path('stats/', views.stat_page, name="statistics")
]