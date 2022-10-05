from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, display_user, edit_user, delete_user

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('profile/<int:pk>/', include([
        path('', display_user, name='display user'),
        path('edit/', edit_user, name='edit user'),
        path('delete/', delete_user, name='delete user'),
    ])),
)
