from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, display_user, edit_user, delete_user

urlpatterns = (
    path('register/', register_user),
    path('login/', login_user),
    path('profile/<int:pk>/', include([
        path('', display_user),
        path('edit/', edit_user),
        path('delete/', delete_user),
    ])),
)
