from django.urls import path
from . import views
#انشاء مسار لصفحات التي كتبنا وظيقتها في ملف views.py
urlpatterns = [
    path('', views.home, name='blog-home'),
    path( 'about/', views.about, name='blog-about' ),

]