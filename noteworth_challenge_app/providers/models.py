from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    given_name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} {self.given_name} {self.family_name} {self.clinic}"
