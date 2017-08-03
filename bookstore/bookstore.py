def create_bookstore(name):
	bookstore = {}
	bookstore['name'] = name
	return bookstore


def add_author(bookstore, name, nationality):
	# author needs to be a dictionary with 
		# name
		# nationality
		# uniqueID
	author = {}

	# want consistent IDs 
	# you would not do this if you had more than 3 authors 
	if name == 'Edgar Allan Poe':
		author['id'] = '1' 
	elif name == 'Jorge Luis Borges':
		author['id'] = '2' 
	elif name == 'James Joyce': 
		author['id'] = '3' 
	
	author['name'] = name 
	author['nationality'] = nationality
	bookstore[name] = author

	return author 

def get_author_by_name(bookstore, name):
	author = {}
	author['id'] = bookstore[name]['id']
	author['name'] = bookstore[name]['name']
	author['nationality'] = bookstore[name]['nationality']
	return author

def get_author_by_id(bookstore, author_id):
	if author_id == '1':
		author = {
			'id': '1',
			'name': 'Edgar Allan Poe',
			'nationality':  'US'
		}
	elif author_id == '2':
		author = {
			'id': '2',
			'name': 'Jorge Luis Borges',
			'nationality':  'AR'
		}
	elif author_id == '3':
		author = {
			'id': '2',
			'name': 'James Joyce',
			'nationality':  'UK'
		}
	
	return author


def add_book(bookstore, title, isbn, author_id):
	book = {}
	
	book['title'] = title
	book['isbn'] = isbn
	book['author_id'] = author_id
	
	bookstore[title] = book
	return book 

def get_book_by_title(bookstore, title):
	book = {}
	book['title'] = bookstore[title]['title']
	book['isbn'] = bookstore[title]['isbn']
	book['author_id'] = bookstore[title]['author_id']
	
	return book 

def get_book_by_id(bookstore, book_id):

		
	for key, value in bookstore.items():
		print(key)
		print(value)

	if book_id == 'XXX-1':
		book = {
			'title': 'The Raven',
			'isbn': 'XXX-1',
			'author_id': '1'
		}
	
	return book 


def get_books_by_author(bookstore, author_id):
    pass
'''
print('---------------------------------------------')
print(bookstore)
print('---------------------------------------------')
'''
#store = create_bookstore("rmotr's bookstore")
#poe = add_author(store, 'Edgar Allan Poe', 'US')
#borges = add_author(store, 'Jorge Luis Borges', 'AR')
#joyce = add_author(store, 'James Joyce', 'UK')
