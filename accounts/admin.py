from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import (
    UserAdminCreationForm,
    UserAdminChangeForm,
    SellerAdminChangeForm,
    SellerAdminCreationForm,
    CustomerAdminChangeForm,
    CustomerAdminCreationForm,
    DriverAdminChangeForm,
    DriverAdminCreationForm,
    ModeratorAdminChangeForm,
    ModeratorAdminCreationForm,
    AdminChangeForm,
    AdminCreationForm
)
from .models import (
    User,
    Seller, SellerMore,
    Customer, CustomerMore,
    Driver, DriverMore,
    Moderator, ModeratorMore,
    Admin, AdminMore,
)


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'type')}
         ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('username',)
    filter_horizontal = ()


class SellerAdmin(BaseUserAdmin):
    form = SellerAdminChangeForm
    add_form = SellerAdminCreationForm

    list_display = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


class CustomerAdmin(BaseUserAdmin):
    form = CustomerAdminChangeForm
    add_form = CustomerAdminCreationForm

    list_display = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


class DriverAdmin(BaseUserAdmin):
    form = DriverAdminChangeForm
    add_form = DriverAdminCreationForm

    list_display = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


class ModeratorAdmin(BaseUserAdmin):
    form = ModeratorAdminChangeForm
    add_form = ModeratorAdminCreationForm

    list_display = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


class AdminForm(BaseUserAdmin):
    form = AdminChangeForm
    add_form = AdminCreationForm

    list_display = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Moderator, ModeratorAdmin)
admin.site.register(Admin, AdminForm)

admin.site.register(SellerMore)
admin.site.register(CustomerMore)
admin.site.register(DriverMore)
# admin.site.register(ModeratorMore)
# admin.site.register(AdminMore)
