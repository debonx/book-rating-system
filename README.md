# Book Rating System

A simple python software to analyse books and users who have read them. Accomplished at [Codeacademy](https://www.codecademy.com/) PRO Intensive class. Thanks to [addubinski](https://github.com/addubinski)

## Classes

### User(name, email)

Creates a user object with the following methods:
- **get_email()**: returns email address
- **change_email(address)**: changes user email
- **read_book(book, rating=None)**: adds book to user and assigns a rating
- **get_average_rating()**: returns the user average rating given to books
- **__repr__()**: returns representaiton string
- **__eq__(other_user)**: checks for doubled user objects

### Book(title: str, isbn: int)

Creates a book object with the following methods:
- **get_title()**: returns book title
- **get_isbn()**: returns book's isbn
- **set_isbn()**: set book's isbn
- **add_rating(rating)**: assigns rating to the book
- **get_average_rating()**: gets average rating given to this book
- **__eq__(other_book)**: checks if the book already exists
- **__hash__()**: makes object hashable

### Fiction(author)

Subclass of Book() with the following methods:
- **get_author()**: returns author of Fiction()
- **__repr__()**: representation of Fiction() object

### Non_Fiction(subject, level)

Subclass of Book() with the following methods:
- **get_subject()**: returns subject of Non Fiction
- **get_level()**: returns level of Non Fiction
- **__repr__()**: representation of Non_Fiction() object


### TomeRater()

Class to analyse everything so far. Methods:
- **create_book(title, isbn)**: creates Book() and returns it
- **create_novel(title, author, isbn)**: creates Fiction() and returns it
- **create_non_fiction(title, subject, level, isbn)**: creates Non_Fiction() and returns it
- **add_book_to_user(book, email, rating=None)**: adds book to a user and gives a rating
- **add_user(name, email, user_books=None)**: adds a user
- **print_catalog()**: prints all books added so far
- **print_users()**: prints all users added so far
- **get_most_read_book()**: gets the book read more times
- **highest_rated_book()**: gets the highest rated book
- **most_positive_user()**: returns the users with the most generous ratings

## Enjoy and support!

If you like the project please follow me on [Twitter](https://twitter.com/_huraji) and [Instagram](https://www.instagram.com/huraji/), or endorse on [Linkedin](https://www.linkedin.com/in/emanueledeboni). I'd really appreciate it. If you have still some free time check also [Xilab](https://xilab.co).