from django.urls import path, include

from forms_demos2.web.views import index, list_persons, create_person

urlpatterns = (
    path('', index, name='index'),
    path('persons/', include([
        path('', list_persons, name='list persons'),
        path('create/', create_person, name='create person'),
    ]),
         )
)
