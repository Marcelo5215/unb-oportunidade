from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Curso)
admin.site.register(models.InteresseEmVaga)
admin.site.register(models.Usuario)
admin.site.register(models.Vaga)
admin.site.register(models.Turno)


class EmpresaAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ('cnpj', 'razao_social', 'nome_fantasia', 'usuario', 'imagem')

class ContratoInfoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'matricula')

admin.site.register(models.Empresa, EmpresaAdmin)
admin.site.register(models.ContratoInfo, ContratoInfoAdmin)
