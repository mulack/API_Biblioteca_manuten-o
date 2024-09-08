from django.contrib import admin
from API_Biblioteca.models import Livro, Leitor, Emprestimo


class LivroAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'data_pub', 'categoria']
    ordering = ['titulo',]


class LeitorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'idade', 'cidade']
    ordering = ['nome', ]


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['leitor', 'livro', 'data_emprestimo', 'data_devolucao']
    ordering = ['leitor',]


admin.site.register(Leitor, LeitorAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)



