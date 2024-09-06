from django.db import models

class Post(models.Model):
    categoria = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=600)
    subtitulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=1200)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo
    