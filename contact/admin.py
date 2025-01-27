from django.contrib import admin
from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Display do painel administrativo
    list_display = 'id', 'first_name', 'last_name', 'phone',
    # Ordem decrescente
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 10
    list_max_show_all = 50
    # Torna os itens editáveis sem precisar sair do display
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',