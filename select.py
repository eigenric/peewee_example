from models import Book


def show_books():

	for i, book in enumerate(Book.select()):

	    print("Libro " + str(i) )
	    print("\t Titulo: " + book.title )
	    print("\t Author: " + book.author)


if __name__ == '__main__':

	show_books()
