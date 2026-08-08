from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cpf',
        'phone',
        'issue_date',
        'expiration_date',
    )
    search_fields = (
        'name',
        'cpf',
        'phone',
    )
