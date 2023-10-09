from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import AccountCreationForm, AccountChangeForm
from .models import Account, OtpRegister


# Register your models here.
class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ('first_name', 'is_staff', 'is_active',)
    list_filter = ('phone_number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('account_type', 'email', 'password', 'first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    # raw_id_fields = ('city', 'state', 'country')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
admin.site.register(OtpRegister)
