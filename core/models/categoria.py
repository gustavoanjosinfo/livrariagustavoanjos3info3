from django.db import models

<<<<<<< HEAD

class Categoria(models.Model):  
    descricao = models.CharField(max_length=100)
    
=======
class Categoria(models.Model):
    descricao = models.CharField(max_length = 255)

>>>>>>> 5f2b6d4eac6d76b3948e0560531bf86d57f3f0cf
    def __str__(self):
        return self.descricao