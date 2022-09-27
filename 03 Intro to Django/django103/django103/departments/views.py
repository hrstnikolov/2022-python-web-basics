from random import choice
from django.http import HttpResponse
from django.shortcuts import render, redirect


def demo_view(request, *args, **kwargs):
    print(args)
    print(kwargs)


def demo_view_html(request, *args, **kwargs):
    request_details = [
        args,
        kwargs,
        request.method,
        request.GET,  # query parameters
        request.POST,  # empty
        request.get_port(),
        request.get_host(),
        request.get_full_path(),
        request.headers,
    ]

    body = '<br><br>'.join(str(r) for r in request_details)

    return HttpResponse(body)


def demo_view_render(request):
    context = {
        "method": request.method,
        "order_by": request.GET.get(key="order_by", default="default order of departments")
    }

    return render(
        request=request,
        template_name="departments/all.html",
        context=context,
    )


def demo_view_redirect(request):
    filter_variables = ["department_name", "department_id", "department_group"]
    random_variable = choice(filter_variables)

    to = f"/departments/render-demo?order_by={random_variable}"
    to = "https://bgonair.bg"

    return redirect(to=to)
