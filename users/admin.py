from django.contrib import admin
from users.models import User, CodeRecoverPassword


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'username', 'email')
    search_fields = ('username', 'email')
