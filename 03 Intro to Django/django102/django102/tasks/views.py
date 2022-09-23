from django.http import HttpResponse
from django.shortcuts import render

from django102.tasks.models import Task


# Create your views here.

def index(request):
    return HttpResponse("<h1>It works!</h1>")


def show_all_tasks_as_http_response(request):
    all_tasks = Task.objects.order_by("priority").all()
    tasks_to_show = "\r".join([f"{t.id}.  {t.name}, {t.description}" for t in all_tasks])

    return HttpResponse(tasks_to_show)


def show_all_tasks_as_rendered_template(request):
    tasks = Task.objects.order_by("id").all()
    context = {
        "tasks": tasks,
    }

    return render(
        request=request,
        template_name="all_tasks.html",
        context=context,
    )
