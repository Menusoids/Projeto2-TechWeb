from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Avaliacao(models.Model):
    rawg_id = models.IntegerField(unique=True)
    nome_jogo = models.CharField(max_length=200)
    capa_url = models.URLField(max_length=500, blank=True)
    nota = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    resenha = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-atualizado_em']

    def __str__(self):
        return f'{self.nome_jogo} ({self.nota}/5)'
