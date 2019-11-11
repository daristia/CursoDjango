
from django.urls import path
from core import views as core_views
from services import views as services_views

urlpatterns = [
    path('',core_views.home, name="home"),
    path('about/',core_views.about, name="about"),
    path('services/',services_views.services, name="services"),
    path('store/',core_views.store, name="store"),
]
