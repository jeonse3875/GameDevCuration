from . import views
from django.urls import path

urlpatterns = [
    path('', views.DevInformationView.as_view(),name='devinfo'),
]