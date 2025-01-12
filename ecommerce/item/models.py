from django.db import models
from django.contrib.auth.models import User


class Catagory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name


class Item(models.Model):
    catagory = models.ForeignKey(
        Catagory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='items', on_delete=models.CASCADE)
