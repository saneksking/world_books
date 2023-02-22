from django.contrib import admin
from . import models

# admin.site.register(models.Author)
# admin.site.register(models.Book)
admin.site.register(models.Genre)
admin.site.register(models.Language)
admin.site.register(models.Status)
# admin.site.register(models.BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name',
              ('date_of_birth', 'date_of_death')]


# @admin.register(models.Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'genre', 'language', 'display_author')
#     list_filter = ('genre', 'author')


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экзепляр книги', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),
    )


class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'genre', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]


admin.site.register(models.Author, AuthorAdmin)
