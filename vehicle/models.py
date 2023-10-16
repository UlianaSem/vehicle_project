from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name="цена", **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "автомобиль"
        verbose_name_plural = "автомобили"


class Moto(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name="цена", **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "мотоцикл"
        verbose_name_plural = "мотоциклы"


class Milage(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, verbose_name="мотоцикл", related_name='milage', **NULLABLE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="автомобиль", **NULLABLE)

    distance = models.PositiveIntegerField(verbose_name="километраж")
    year = models.CharField(max_length=4, verbose_name="год")

    def __str__(self):
        if self.moto:
            return f"{self.moto} ({self.distance}, {self.year})"

        return f"{self.car} ({self.distance}, {self.year})"

    class Meta:
        verbose_name = "пробег"
        verbose_name_plural = "пробег"
        ordering = ("-year",)
