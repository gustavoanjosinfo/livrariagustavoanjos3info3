from django.db import models

<<<<<<< HEAD

=======
>>>>>>> 5f2b6d4eac6d76b3948e0560531bf86d57f3f0cf
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"