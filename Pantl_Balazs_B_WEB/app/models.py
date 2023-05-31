from django.db import models

class Tema(models.Model):
    tema_id = models.AutoField(primary_key=True, editable= False)
    temanev = models.CharField(verbose_name="temanev", max_length=50)

    def __str__(self):
        return self.temanev


class Szavak(models.Model):
    szavak_id = models.AutoField(primary_key=True, editable= False)
    angol = models.CharField(verbose_name="angol", max_length=100)
    magyar = models.CharField(verbose_name="magyar", max_length=100)
    temaId = models.ForeignKey(Tema, on_delete=models.CASCADE, verbose_name="temaId")

    def __str__(self):
        return f'{self.angol} | {self.magyar}'