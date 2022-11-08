from django import forms

from forms_demos.web.models import Person


class NameForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        label='Your name:',
        help_text='Please enter your name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Вашето име...',
            },
        )
    )
    age = forms.IntegerField(
        label='Age',
        help_text='Please enter your age',
    )

    married = forms.BooleanField(required=False)

    email = forms.CharField(
        widget=forms.EmailInput(),
    )


class NameForm2(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
