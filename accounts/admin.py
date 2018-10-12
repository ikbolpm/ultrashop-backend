from django.contrib import admin
from django.contrib.auth import get_user_model, admin as user_admin
from django.utils.translation import gettext_lazy as _

from accounts.models import User

admin.site.register(User, user_admin.UserAdmin)
