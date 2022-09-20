from django.urls import path, include

from django101.tasks.views import view

urlpatterns = [
    path("", view),
]