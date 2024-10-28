from django.contrib import admin
from django.urls import path

from feedback import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('feedback/', views.feedback, name='feedback'),
]
