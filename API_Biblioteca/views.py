from rest_framework import viewsets, permissions
from API_Biblioteca.models import *
from API_Biblioteca.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class LivroAPI(viewsets.ModelViewSet):
    '''API para gerenciamento de livros'''
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class LeitorAPI(viewsets.ModelViewSet):
    '''API para gerenciamento de leitores'''
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    # traz todos os emprestimos de um usuario
    @action(detail=True, methods=['get'])
    def emprestimos(self, request, pk=None):
        leitor = self.get_object()
        emprestimos = Emprestimo.objects.filter(leitor=leitor)
        serializer = EmprestimoSerializer(emprestimos, many=True)
        return Response(serializer.data)


class EmprestimoAPI(viewsets.ModelViewSet):
    '''API para gerenciamento de emprestimos'''
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

