from django.urls import path

from django102.tasks.views import index, show_all_tasks_as_http_response, show_all_tasks_as_rendered_template

urlpatterns = (
    path('', index),
    path('all/', show_all_tasks_as_rendered_template),
)
