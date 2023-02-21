from django.shortcuts import render, HttpResponse
from . import models


def index(request):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_instances_available = models.BookInstance.objects.filter(status_exact=2).count()
    num_authors = models.Author.objects.count()
    context = {'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'num_authors': num_authors}
    return render(request, 'index.html', context=context)
