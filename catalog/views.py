from django.shortcuts import render

from catalog.models import BookInstance, Book, Author, Genre
# Create your views here.

def indext(request):
    num_of_books        = Book.objects.all().count()
    num_of_instances    = BookInstance.objects.all().count()
    
    # Available books (status = a)  
    num_of_instances_avaiable = BookInstance.objects.filter(stauts__exact='a').count()
    
    num_of_authors = Author.objects.all().count()
    
    context = {
        'num_of_books' : num_of_books,
        'num_of_instances' : num_of_instances,
        'num_of_instances_avaiable' : num_of_instances_avaiable,
        'num_of_authors': num_of_authors,
    }
    
    return render(request, 'index.html', context)
    
