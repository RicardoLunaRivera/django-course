from django.contrib import admin
from .models import Curso, Docente

# Register your models here.


@admin.register(Curso)
class CursoAdmin (admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos')
    # ordering = ('-nombre', )
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('creditos',) # s epuede colocar que campoe stá disponible para edicion
    # list_display_links = ('nombre',) # crea el link de redireccionamiento a el panel de edicion
    # list_filter = ('creditos',)
    # list_per_page = 3  # crea una paginación
    # exclude = ('creditos',)  # no permite editar el campo indicado
# admin.site.register(Curso)
# admin.site.register(Curso, CursoAdmin)


admin.site.register(Docente)
