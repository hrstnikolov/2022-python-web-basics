from django.urls import path

from models_demo.web.views import index, department_details, delete_employee, show_employees, employee_details

urlpatterns = (
    path('', index, name='index'),
    path('employees/', show_employees, name='show employees'),
    path('employee/<int:pk>/', employee_details, name='employee details'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),

    # http://localhost:8000/departments/1/engineering/
    path('departments/<int:pk>/<slug:slug>/', department_details, name='department details'),
)
