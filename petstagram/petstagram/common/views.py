from django.shortcuts import render

from petstagram.photos.models import Photo


# TODO: update when implementing auth
def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


# TODO: update when implementing auth
def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    pass