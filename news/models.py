from django.db import models

from django.db import models


class Articles(models.Model):
    title = models.CharField("Nomlanishi", max_length=500)
    anons = models.CharField("Anons", max_length=2500)
    full_text = models.TextField("Statya")
    date = models.DateTimeField("Chiqarilgan sana")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


