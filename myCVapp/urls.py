from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('pdf_view/', views.pdf_view, name='pdf_view'),
]
    