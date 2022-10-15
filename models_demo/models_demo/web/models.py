import datetime

from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Manager(models.Model):
    MANAGER_LEVELS = [
        (1, 'Supervisor'),
        (2, 'Manager'),
        (3, 'Director'),
    ]

    first_name = models.CharField(
        max_length=30,
        verbose_name='First name'
    )

    level = models.IntegerField(
        choices=MANAGER_LEVELS,
        verbose_name='Proficiency level',
        null=True,
    )

    has_private_office = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Private office?',
    )

    salary = models.FloatField(
        editable=False,
        null=True,
    )

    def __str__(self):
        return f'{self.first_name} ({self.get_level_display()})'


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    age = models.IntegerField(default=-1)
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        default=1,
    )
    manager = models.ForeignKey(to=Manager, on_delete=models.RESTRICT)

    years_of_experience = models.PositiveIntegerField(null=True, blank=True, )
    review = models.TextField(null=True, blank=True, )
    city = models.CharField(max_length=40, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Id: {self.pk}, {self.name_and_age}'

    @property
    def time_in_the_company(self):
        return datetime.date.today() - self.created_on.date()

    @property
    def name_and_age(self):
        return f'{self.first_name}, {self.age}'

    def get_absolute_url(self):
        url = reverse('employee details', kwargs={'pk':self.pk})
        return url

class Project(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ManyToManyField(to=Employee)


class AccessCard(models.Model):
    employee = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    card_type = models.CharField(max_length=30, null=True, blank=True)
