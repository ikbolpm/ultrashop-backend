from django.contrib import admin
from django.contrib.auth import get_user_model, admin as user_admin

User = get_user_model()

class UserAdmin(user_admin.UserAdmin):
    search_fields = ['email']
    list_display = ['email', 'is_staff', 'is_admin', 'last_login', 'created']

    class Meta:
        model = User

admin.site.register(User, UserAdmin)
