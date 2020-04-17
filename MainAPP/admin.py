from django.contrib import admin


class LocationUsersInLine(admin.TabularInline):
    extra = 0

    class StatusAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_active']

    class UserAdmin(admin.ModelAdmin):
        list_display = ['customer_name', 'customer_phone', 'customer_email', 'customer_address', 'comments', 'status']

