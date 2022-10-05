from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=-1)
    city = models.CharField(max_length=40, null=True)
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        default=1,
    )

    @property
    def name_and_age(self):
        return f'{self.first_name}, {self.age}'

    def __str__(self):
        return f'Id: {self.pk}, {self.name_and_age}'


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


class Project(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ManyToManyField(to=Employee)
