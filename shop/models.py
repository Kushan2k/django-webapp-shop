from django.db import models
from django.contrib.auth.models import User
# Create your models here


class Item(models.Model):
    name = models.CharField(max_length=90)
    post_date = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self) -> str:
        return f'({self.name})'


class Images(models.Model):
    url = models.FileField(upload_to='item_images')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.url}'


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.item.id})'
