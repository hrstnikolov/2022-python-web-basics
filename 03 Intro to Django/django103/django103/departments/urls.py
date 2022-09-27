from django.urls import path
from django103.departments.views import demo_view, demo_view_html, demo_view_render, demo_view_redirect

urlpatterns = (
    path('', demo_view),
    path('int/<int:department_id>/', demo_view_html),
    path('render-demo/', demo_view_render),
    path('redirect-demo/', demo_view_redirect),
)
