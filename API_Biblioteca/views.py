from rest_framework import viewsets, permissions
from API_Biblioteca.models import *
from API_Biblioteca.serializers import *
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class Livro_API(viewsets.ModelViewSet):
    '''API para gerenciamento de livros'''
    queryset = Livro.objects.all()
    serializer_class = Livro_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class Leitor_API(viewsets.ModelViewSet):
    '''API para gerenciamento de leitores'''
    queryset = Leitor.objects.all()
    serializer_class = Leitor_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

