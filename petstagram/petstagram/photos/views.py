from django.shortcuts import render, redirect

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def edit_photo(request, photo_pk):
    return render(request, 'photos/photo-edit-page.html')


def display_photo(request, photo_pk):
    photo = Photo.objects.get(pk=photo_pk)
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }
    return render(request, 'photos/photo-details-page.html', context)


def delete_photo(request, photo_pk):
    Photo.objects.get(pk=photo_pk).delete()
    return redirect('index')
