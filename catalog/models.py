from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter genre book', verbose_name='Genre book')

    def __str__(self):
        return self.name


class Language(models.Model):
    lang = models.CharField(max_length=20,
                            help_text='Enter book language',
                            verbose_name='Book language')

    def __str__(self):
        return self.lang


class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Enter author's name",
                                  verbose_name="Author's name")
    last_name = models.CharField(max_length=100,
                                 help_text="Enter author's surname",
                                 verbose_name="Author's surname")
    date_of_birth = models.DateField(help_text='Enter date of birthday',
                                     verbose_name='Date of birthday',
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text='Enter date of death',
                                     verbose_name='Date of death',
                                     null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100,
                             help_text="Enter book's title",
                             verbose_name="Book's title")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text='Choose genre  for book',
                              verbose_name="Book's genre", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text="Choose book's language",
                                 verbose_name="Book's language", null=True)
    author = models.ManyToManyField('Author',
                                    help_text="Choose book's author",
                                    verbose_name="Book's author")
    summary = models.TextField(max_length=1000,
                               help_text='Enter short description book',
                               verbose_name="Book's annotation")
    isbn = models.CharField(max_length=13,
                            help_text='Must contain 13 chars',
                            verbose_name="Book's ISBN")

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Enter book's copy status",
                            verbose_name='Status copy book')

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text="Enter copy's inventory number",
                               verbose_name='Inventory number')
    imprint = models.CharField(max_length=200,
                               help_text="Enter publishing house and release year",
                               verbose_name='Publishing house')
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text="Changes copy's status",
                               verbose_name="Book copy's status")
    due_back = models.DateField(null=True, blank=True,
                                help_text="Enter end of status's term",
                                verbose_name="Date of status end")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
