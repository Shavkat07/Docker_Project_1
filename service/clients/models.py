from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=265)
    full_address = models.CharField(max_length=299)

    def __str__(self):
        return f'Compoany  name {self.company_name}'
