from django.contrib import admin
from blogUser.models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class customUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('-id',)
    readonly_fields = 'super_user_code',