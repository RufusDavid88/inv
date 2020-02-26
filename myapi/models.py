from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone

class Lowerparel(models.Model):
    DEV_CHOICES = (
        ('DESKTOP','DESKTOP'),
        ('LAPTOP','LAPTOP'),
    )
    DEV_MOUSE = (
        ('Yes','yes'),
        ('No','no'),
    )


    new_joinee = models.CharField(max_length=60)
    designation = models.CharField(max_length=60,null=True)
    current_ou = models.CharField(max_length=60)
    date_of_joinee = models.DateField(default=timezone.now)
    current_ou_removed = models.CharField(max_length=60)
    device_assigned = models.CharField(max_length=60,choices=DEV_CHOICES,null=True)
    mouse_assigned = models.CharField(max_length=60,choices=DEV_MOUSE,null=True)

    def __str__(self):
        return self.new_joinee


class Bhiwandi (models.Model):
    DEV_CHOICES1 = (
        ('DESKTOP','DESKTOP'),
        ('LAPTOP','LAPTOP'),
    )

    DEV_MOUSE1 = (
        ('Yes', 'yes'),
        ('No', 'no'),
    )

    new_joinee = models.CharField(max_length=60)
    designation = models.CharField(max_length=60,null=True)
    current_ou = models.CharField(max_length=60)
    date_of_joinee = models.DateField(default=timezone.now)
    current_ou_removed = models.CharField(max_length=60)
    device_assigned = models.CharField(max_length=60,choices=DEV_CHOICES1,null=True)
    mouse_assigned = models.CharField(max_length=60,choices=DEV_MOUSE1,null=True)


    def __str__(self):
        return self.new_joinee



class STORE (models.Model):
    new_joinee = models.CharField(max_length=60)
    date_of_joinee = models.DateField(default=timezone.now)
    device_assigned = models.CharField(max_length=60)
    mouse_assigned = models.CharField(max_length=60)


    def __str__(self):
        return self.new_joinee