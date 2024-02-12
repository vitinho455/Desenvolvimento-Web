from django.contrib import admin
#Modelos Criados e importado
from PCs.models import Desktop 

#Modelo Desktop
class DesktopAdmin(admin.ModelAdmin):

    list_display = ('Processador', 'MemoriaRam', 'PlacaDeVideo', 'FonteDeEnergia', 'Gabinete', 'Memoria', 'Valor','Descricao')
    search_fields = ('Processador', 'MemoriaRam', 'PlacaDeVideo', 'FonteDeEnergia', 'Gabinete', 'Memoria', 'Valor', 'Descricao')
    
admin.site.register(Desktop, DesktopAdmin)
