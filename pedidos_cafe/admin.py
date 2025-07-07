from django.contrib import admin
from pedidos_cafe.models import PedidoCafe

class PedidoCafeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.full_clean()  # Esto ejecuta el método clean() del modelo antes de guardar cambios
        super().save_model(request, obj, form, change)

admin.site.register(PedidoCafe, PedidoCafeAdmin)