from django.db import models


class Veiculo(models.Model):
    modelo = models.ForeignKey('core.Modelo', on_delete=models.CASCADE)
    cor = models.ForeignKey('core.Cor', on_delete=models.CASCADE)
    ano = models.IntegerField(null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    acessorios = models.ManyToManyField('core.Acessorio')

    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.cor} - {self.ano} - {self.preco} - {self.acessorios}'
