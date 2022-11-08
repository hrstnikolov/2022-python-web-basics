from django import forms
from django.core.exceptions import ValidationError

from forms_demos2.web.models import TodoModel, Person
from forms_demos2.web.validators import ValueInRangeValidatorForForms, validate_text


class TodoForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        validators=(
            validate_text,
        ),
    )

    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        required=False,
        validators=(
            # validate_priority,
            # ValueInRangeValidator(1, 10),
            ValueInRangeValidatorForForms(1, 10),
        ),
    )


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'

    def clean(self):
        print('asd')
        return super().clean()

    def clean_assignee(self):
        ASSIGNEE_MAX_TODO_COUNT = 2
        assignee = self.cleaned_data['assignee']

        if assignee.todos.count() > ASSIGNEE_MAX_TODO_COUNT:
            raise ValidationError(f'Max {ASSIGNEE_MAX_TODO_COUNT} todo items allowed per person.')

        return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
