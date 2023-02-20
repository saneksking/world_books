from django.contrib import admin
from . import models

# admin.site.register(models.Author)
# admin.site.register(models.Book)
admin.site.register(models.Genre)
admin.site.register(models.Language)
admin.site.register(models.Status)
# admin.site.register(models.BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')


admin.site.register(models.Author, AuthorAdmin)
