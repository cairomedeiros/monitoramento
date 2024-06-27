from django.db import models

class Luz(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=False)  # False para desligado, True para ligado
    brilho = models.IntegerField(default=0)  # Brilho da luz, de 0 a 100

    def __str__(self):
        return self.name

