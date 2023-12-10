from django.db import models


class Record(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=6)

    def __str__(self):
        return (f"{self.firstName} {self.lastName}")
