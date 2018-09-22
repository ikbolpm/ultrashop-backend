from django.contrib import admin
from django.contrib.auth import get_user_model, admin as user_admin

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['email', 'is_staff', 'is_admin', 'last_login', 'created']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('full_name',  )}),
        (_('Permissions'), {'fields': ('is_active', 'staff', 'admin', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created')}),
    )
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
