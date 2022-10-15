from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from models_demo.web.models import Employee, Project
import re


def index(request):
    context = {
        # 'employees': [e for e in Employee.objects.all() if e.department.name.startswith('D')],
        # 'employees2': Employee.objects.filter(department__name__startswith="D"),
        'employees': Employee.objects.all(),
        'first_project': Project.objects.get(pk=1),
    }
    return render(request, 'index.html', context)


def department_details(request, pk, slug):
    context = {
        "pk": pk,
        "slug": slug,
    }
    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')


def show_employees(request):
    # fields = [re.search(r'\.[^\.]+$', f).group(0) for f in Employee._meta.fields]

    context = {
        'employees': Employee.objects.all(),
        'fields': Employee._meta.fields,
    }
    return render(request, 'show-employees.html', context)


def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee,
    }
    return render(request, 'employee-details.html', context)
