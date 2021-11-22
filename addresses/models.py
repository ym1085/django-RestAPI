from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_date']
