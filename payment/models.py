from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    price = models.IntegerField(default= 0)

    def __str__(self):
        return self.name