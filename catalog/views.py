from django.shortcuts import render
from django.views import generic

from catalog.models import BookInstance, Book, Author, Genre
# Create your views here.

def index(request):
    num_of_books        = Book.objects.all().count()
    num_of_instances    = BookInstance.objects.all().count()
    
    # Available books (status = a)  
    num_of_instances_avaiable = BookInstance.objects.filter(status__exact='a').count()
    
    num_of_authors = Author.objects.all().count()
    
    context = {
        'num_of_books' : num_of_books,
        'num_of_instances' : num_of_instances,
        'num_of_instances_avaiable' : num_of_instances_avaiable,
        'num_of_authors': num_of_authors,
    }
    
    return render(request, 'index.html', context)
    

# CLASS BASED VIEWS
class BookListView(generic.ListView):
    model = Book
    
    
#     # django will look for the corresponding template: modelname_list in the app
#     # so for this django will look for templates/catalog/book_list.html

# def bookList_view(request):
#     booklist = Book.objects.all()
#     context = {
#         'booklist': booklist
#     }
#     return render(request, 'book_list.html', context)

def bookdetail_view(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        raise Http404('The book does not exist')
    context = {
        'book':book,
    }
    return render(request, 'book_detail.html', context)