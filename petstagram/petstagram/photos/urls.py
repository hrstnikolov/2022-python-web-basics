from django.urls import path, include
from petstagram.photos.views import add_photo, display_photo, edit_photo, delete_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('<int:photo_pk>/', include([
        path('', display_photo, name='display photo'),
        path('edit/', edit_photo, name='edit photo'),
        path('delete/', delete_photo, name='delete photo'),
    ])),
)
