from django.urls import path

from petstagram.common.views import index, like_photo, copy_link_to_clipboard

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share photo'),
)
