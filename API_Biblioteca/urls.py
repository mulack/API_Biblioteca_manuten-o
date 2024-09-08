from rest_framework.routers import SimpleRouter
from API_Biblioteca.views import *

# gerador automático de urls do rest
router = SimpleRouter()
router.register('livros', LivroAPI)
router.register('leitores', LeitorAPI)
router.register('emprestimos', EmprestimoAPI)

urlpatterns = [
    # outras urls do seu projeto
    
]