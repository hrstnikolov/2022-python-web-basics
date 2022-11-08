from django.urls import path

from forms_demos.web.views import index, index2, update_employee

urlpatterns = (
    path('', index, name='index'),
    path('modelforms/', index2, name='model forms'),
    path('employee/<int:pk>/', update_employee, name='update employee'),

)