from django.db import models


class Catalog(models.Model):
    photo = models.ImageField(
        upload_to='house_photo/',
        blank=True,
    )
    description = models.TextField(max_length=300)
    price = models.DecimalField(
        max_digits=10,   # количество цифр во всех номерах.
        decimal_places=0  # количество цифр справа от запятой.
    )

    def __str__(self):
        return self.description
