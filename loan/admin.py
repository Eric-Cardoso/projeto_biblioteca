from django.contrib import admin

from loan.models import LoanDuration, Loan


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