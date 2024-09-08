from rest_framework import serializers
from API_Biblioteca.models import *

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'data_pub']


class LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = ['id', 'nome', 'idade', 'cidade'] 


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'leitor', 'livro', 'data_emprestimo', 'data_devolucao']