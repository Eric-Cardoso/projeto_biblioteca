from django.contrib import admin

from loan.models import LoanDuration, Loan
from book.models import Book


@admin.register(LoanDuration)
class LoanDurationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('client', 'book', 'loan_date',)
    search_fields = (
        'client__name', 
        'client__cpf', 
        'book__name', 
        'book__author', 
        'book__genre__name',
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'book' and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = Book.objects.filter(was_loaned=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)