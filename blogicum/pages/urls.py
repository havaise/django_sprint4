from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutPages.as_view(), name='about'),
    path('rules/', views.RulesPages.as_view(), name='rules')
]
