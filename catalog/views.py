from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from catalog.models import BookInstance, Book, Author, Genre
# Create your views here.

def index(request):
    num_of_books        = Book.objects.all().count()
    num_of_instances    = BookInstance.objects.all().count()
    
    
    
    # Available books (status = a)  
    num_of_instances_avaiable = BookInstance.objects.filter(status__exact='a').count()
    
    num_of_authors = Author.objects.all().count()
    
    num_of_views = request.session.get('num_of_views', 0)
    request.session['num_of_views'] =  num_of_views + 1
    
    context = {
        'num_of_books' : num_of_books,
        'num_of_instances' : num_of_instances,
        'num_of_instances_avaiable' : num_of_instances_avaiable,
        'num_of_authors': num_of_authors,
        'num_of_views': num_of_views,
    }
    
    print("REQUEST ", request)
    
    return render(request, 'index.html', context)
    

# CLASS BASED VIEWS
class BookDetailView(generic.DetailView):
    model = Book
class BookListView(generic.ListView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
     
class AuthorDetailView(generic.DetailView):
    model = Author    


@login_required #import required from django.contrib.auth.decorators
def restricted_view(request):
    response_string = "<h1> This is a restricted view </h1>"
    response_string += "<p> This will only be displayed if you are logged in </p>"
    return HttpResponse(response_string)
    
# the @login_required decorator runs the views only if a user is logged in 
# and autheticated else it will redirect to the login URL in settings.LOGIN_URL
    
#     # django will look for the corresponding template: modelname_list in the app
#     # so for this django will look for templates/catalog/book_list.html

# def bookList_view(request):
#     booklist = Book.objects.all()
#     context = {
#         'booklist': booklist
#     }
#     return render(request, 'book_list.html', context)

# def bookdetail_view(request, id):
#     try:
#         book = Book.objects.get(pk=id)
#     except Book.DoesNotExist:
#         raise Http404('The book does not exist')
#     context = {
#         'book':book,
#     }
#     return render(request, 'book_detail.html', context)


    

