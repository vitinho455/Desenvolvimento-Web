from django.db import models

# Create your models here.

#Classe para Desktops
class Desktop(models.Model):
    id = models.AutoField(primary_key=True)
    Processador = models.CharField(max_length=200)
    MemoriaRam = models.CharField(max_length=200)
    PlacaDeVideo = models.CharField(max_length=200)
    FonteDeEnergia = models.CharField(max_length=200)
    Gabinete = models.CharField(max_length=200)
    Memoria = models.CharField(max_length=200)
    Valor = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='PCs/', blank=True, null=True)
    Descricao = models.TextField(verbose_name='Descrição do Produto')

    def __str__(self):
        return self.Processador
    


