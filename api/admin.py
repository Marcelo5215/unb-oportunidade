from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Curso)
admin.site.register(models.Empresa)
admin.site.register(models.InteresseEmVaga)
admin.site.register(models.Usuario)
admin.site.register(models.Vaga)
admin.site.register(models.ContratoInfo)