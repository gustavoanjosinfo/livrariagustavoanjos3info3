from django.db import models

<<<<<<< HEAD
from core.models import Autor, Categoria, Editora
from uploader.models import Image


class Livro(models.Model):

    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )

=======
class Livro (models.Model):
>>>>>>> 5f2b6d4eac6d76b3948e0560531bf86d57f3f0cf
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
<<<<<<< HEAD
    autores = models.ManyToManyField(Autor, related_name="livros")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
 
    def __str__(self):
        return f'{self.titulo} ({self.quantidade}) - R${self.preco}'
    
    
=======
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, 
    related_name="livros")
    editora = models.ForeignKey (Editora, on_delete=models.PROTECT, related_name='livros')
    

    def __str__(self):
        return f'{self.titulo}({self.quantidade}) - {self.preco}'
>>>>>>> 5f2b6d4eac6d76b3948e0560531bf86d57f3f0cf
