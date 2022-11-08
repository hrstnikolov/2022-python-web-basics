from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


# TODO: fix when auth
def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


# TODO: fix when auth
def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def filter_like_by_user_and_photo(user_id, photo_id):
    # TODO: fix when auth
    return PhotoLike.objects.filter(to_photo=photo_id)


def like_photo(request, photo_id):
    # todo: fix when auth
    liked_photo = filter_like_by_user_and_photo('dummy user', photo_id)
    if liked_photo:
        liked_photo.delete()
    else:
        PhotoLike.objects.create(to_photo_id=photo_id)
        # photo = Photo.objects.get(id=photo_id)
        # PhotoLike.objects.create(to_photo=photo)

    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    # 'http://127.0.0.1:8000/#photo-3'

    return redirect(to=redirect_path)

    # # Option 1
    # photolike = PhotoLike(to_photo_id=photo_id)
    # photolike.save()


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def copy_link_to_clipboard(request, photo_id):
    link_to_photo = request.META['HTTP_HOST'] + resolve_url('display photo', photo_id)
    copy(link_to_photo)

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
