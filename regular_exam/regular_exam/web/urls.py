from django.urls import path, include

from regular_exam.web.views import index, catalogue, \
    create_profile, edit_profile, details_profile, delete_profile, \
    create_car, edit_car, details_car, delete_car


urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/', include([
            path('edit/', edit_car, name='edit car'),
            path('details/', details_car, name='details car'),
            path('delete/', delete_car, name='delete car'),
        ]), )
    ])),
)
