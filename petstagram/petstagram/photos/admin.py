from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'pets')

    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if not tagged_pets:
            return 'No tagged pets.'
        tagged_pets_names = [pet.name for pet in tagged_pets]
        return ', '.join(tagged_pets_names)
