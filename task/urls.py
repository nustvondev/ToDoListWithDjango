from django.urls import path
from . import views
ap_name = 'task'
urlpatterns = [
    path("", views.index, name="index"),
    
]