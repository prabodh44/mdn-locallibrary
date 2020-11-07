from django.contrib import admin

from catalog.models import Author, Genre, Book, BookInstance
# Register your models here.

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)
# registering new models using the @register deocorator
# does the same thing as above

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # adding list filters using list_filter
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields' : ('book', ('id', 'imprint'))}), 
        ('Availability', {
             'fields' : ('status', 'due_back')   
            })
    )

admin.site.register(Genre)
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)

