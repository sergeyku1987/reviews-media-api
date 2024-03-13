from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from users.models import User

UserAdmin.fieldsets += (
    (
        'Extra Fields', {'fields': ('bio', 'role')}
    ),
)

@admin.register(User)
class AdminUser(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email',  'password1', 'password2')}
        ),
    )
    list_per_page = 10
