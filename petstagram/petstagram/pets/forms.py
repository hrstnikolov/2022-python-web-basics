from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_photo',)
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name', }),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to Image', }),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass
