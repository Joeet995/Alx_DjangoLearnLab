from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    firld = UserAdmin.fieldsets + (
        (None, {"fields": ("date of birth", "ptofile photo",)})
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author', 'publication_year')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)