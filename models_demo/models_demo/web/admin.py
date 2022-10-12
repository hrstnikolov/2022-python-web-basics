from django.contrib import admin

from models_demo.web.models import Employee, Manager, Department, Project


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'department', 'years_of_experience', ]
    list_filter = ['department']
    search_fields = ['first_name']
    fieldsets = (
        (
          'Personal Information',
          {'fields': (
              ('first_name', 'age'),
              ('department', 'manager'),
          )},
        ),
        (
          'Additional Information',
          {
              'fields': (
                  ('years_of_experience', 'city',),
                  ('review',),
              ),
              'classes': (
                  'collapse',
              ),
          },
        ),
    )


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'level')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
