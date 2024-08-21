from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author', 'publication_year')

admin.site.register(CustomUserAdmin, CustomUser)
admin.site.register(Book, BookAdmin)