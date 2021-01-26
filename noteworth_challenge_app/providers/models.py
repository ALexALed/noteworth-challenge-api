from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=100)


class Clinic(models.Model):
    name = models.CharField(max_length=300)


class Employee(models.Model):
    given_name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    title = models.ForeignKey(Title)
    clinic = models.ForeignKey(Clinic)
