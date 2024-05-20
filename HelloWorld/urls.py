from . import views
from django.urls import path

urlpatterns = {
    path('', views.helloworld_view, name='hw'),
}