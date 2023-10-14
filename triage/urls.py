from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("view_report/", views.view_report, name="view_report"),
]

