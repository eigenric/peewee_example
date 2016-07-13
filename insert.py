from models import Book

some_books = [('Nietzsche', 'Asi hablo Zaratustra'),
	      ('Pwaqo', 'Conjunto Vacio')]

for abook in some_books:
	
	book = Book()
	book.author, book.title = abook
	book.save()
