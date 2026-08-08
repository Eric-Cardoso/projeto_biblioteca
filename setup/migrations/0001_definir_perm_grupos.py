from django.db import migrations


def define_perm_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    User = apps.get_model('auth', 'User')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    Client = apps.get_model('client', 'Client')
    Book = apps.get_model('book', 'Book')
    BookGenre = apps.get_model('book', 'BookGenre')
    Loan = apps.get_model('loan', 'Loan')
    LoanDuration = apps.get_model('loan', 'LoanDuration')

    client_group, _ = Group.objects.get_or_create(name='clientes')
    book_ct = ContentType.objects.get_for_model(Book)
    perm_view_book = Permission.objects.get(codename='view_book', content_type=book_ct)
    client_group.permissions.set([perm_view_book])

    employee_group, _ = Group.objects.get_or_create(name='funcionários')

    user_ct = ContentType.objects.get_for_model(User)
    cliente_ct = ContentType.objects.get_for_model(Client)
    book_genre_ct = ContentType.objects.get_for_model(BookGenre)
    loan_duration_ct = ContentType.objects.get_for_model(LoanDuration)
    loan_ct = ContentType.objects.get_for_model(Loan)

    perm_add_user = Permission.objects.get(
        codename='add_user',
        content_type=user_ct,
    )
    perm_view_user = Permission.objects.get(
        codename='view_user',
        content_type=user_ct,
    )
    perm_change_user = Permission.objects.get(
        codename='change_user',
        content_type=user_ct,
    )

    perm_add_cliente = Permission.objects.get(
        codename='add_client',
        content_type=cliente_ct,
    )
    perm_view_cliente = Permission.objects.get(
        codename='view_client',
        content_type=cliente_ct,
    )
    perm_change_cliente = Permission.objects.get(
        codename='change_client',
        content_type=cliente_ct,
    )

    perm_add_book_genre = Permission.objects.get(
        codename='add_bookgenre',
        content_type=book_genre_ct,
    )
    perm_view_book_genre = Permission.objects.get(
        codename='view_bookgenre',
        content_type=book_genre_ct,
    )
    perm_change_book_genre = Permission.objects.get(
        codename='change_bookgenre',
        content_type=book_genre_ct,
    )

    perm_add_book = Permission.objects.get(
        codename='add_book',
        content_type=book_ct,
    )
    perm_change_book = Permission.objects.get(
        codename='change_book',
        content_type=book_ct,
    )

    perm_add_loan_duration = Permission.objects.get(
        codename='add_loanduration',
        content_type=loan_duration_ct,
    )
    perm_view_loan_duration = Permission.objects.get(
        codename='view_loanduration',
        content_type=loan_duration_ct,
    )
    perm_change_loan_duration = Permission.objects.get(
        codename='change_loanduration',
        content_type=loan_duration_ct,
    )

    perm_add_loan = Permission.objects.get(
        codename='add_loan',
        content_type=loan_ct,
    )
    perm_view_loan = Permission.objects.get(
        codename='view_loan',
        content_type=loan_ct,
    )
    perm_change_loan = Permission.objects.get(
        codename='change_loan',
        content_type=loan_ct,
    )
    perm_delete_loan = Permission.objects.get(
        codename='delete_loan',
        content_type=loan_ct,
    )

    employee_group.permissions.set(
        [
            perm_add_user,
            perm_add_cliente,
            perm_add_book_genre,
            perm_add_book,
            perm_add_loan_duration,
            perm_add_loan,
            perm_view_user,
            perm_view_cliente,
            perm_view_book_genre,
            perm_view_book,
            perm_view_loan_duration,
            perm_view_loan,
            perm_change_user,
            perm_change_cliente,
            perm_change_book_genre,
            perm_change_book,
            perm_change_loan_duration,
            perm_change_loan,
            perm_delete_loan,
        ]
    )


def remove_perm_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['clientes', 'funcionários']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('book', '0001_initial'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(define_perm_groups, remove_perm_groups),
    ]
