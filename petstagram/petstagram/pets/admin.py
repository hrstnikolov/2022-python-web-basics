from django.contrib import admin

from petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pk_and_name',)

    def pk_and_name(self, current_pet_obj):
        return f'{current_pet_obj.pk:04d} {current_pet_obj.name}'
