from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Categoria, CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]