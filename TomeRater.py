class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.book = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "This users's email has been updated"

    def read_book(self, book, rating=None):
        if rating is not None:
            self.book[book] = rating

    def get_average_rating(self):
        total = 0
        for i in self.book:
            total += self.book[i]
        return total / len(self.book)

    def __repr__(self):
        message = (
            "User {fullname}, "
            "email: {useremail}, "
            "books read: {bnr}".format(
                fullname=self.name, useremail=self.email, bnr=len(self.book)))
        return message

    def __eq__(self, other_user):
        if self.name == other_user.self.name:
            if self.email == other_user.self.email:
                print("This user already exists")


class Book(object):
    def __init__(self, title: str, isbn: int):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn: int):
        self.isbn = new_isbn
        print("This book's isbn has been updated")

    def add_rating(self, rating):
        if rating is not None and rating < 5:
                self.ratings.append(rating)
        else:
            if rating is not None:
                print("Invalid Rating")

    def get_average_rating(self):
        total = 0
        for i in self.ratings:
            total += i
        return total

    def __eq__(self, other_book):
        if self.title == other_book.self.title:
            if self.isbn == other_book.self.isbn:
                print("This book already exists")

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        print("{} by {}".format(self.title, self.author))


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject.title()
        self.level = level.lower()

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        print("{}, a {} manual on {}".format(
            self.title, self.level, self.subject)
        )


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        the_book = Book(title, isbn)
        return the_book

    def create_novel(self, title, author, isbn):
        the_fiction = Fiction(title, author, isbn)
        return the_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        the_non_fiction = Non_Fiction(title, subject, level, isbn)
        return the_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=[None]):
        if email in self.users.keys():
            print("The user with email {} already exists".format(email))
        else:
            self.users[email] = User(name, email)
        for i in user_books:
            if i is not None:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for c in self.books.keys():
            if c is not None:
                print(c.get_title())

    def print_users(self):
        for i in self.users.values():
            print(str(i.__repr__()))

    def get_most_read_book(self):
        times_read = 0
        book_title = ""
        for i in self.books:
            if i is not None:
                if self.books[i] > times_read:
                    times_read = self.books[i]
                    book_title = i.get_title()
        return "{}, {}".format(book_title, times_read)

    def highest_rated_book(self):
        av_rating = 0
        book_title = ""
        for i in self.books.keys():
            if i.get_average_rating() > av_rating:
                av_rating = i.get_average_rating()
                book_title = i.get_title()
        return book_title + ", rated " + str(av_rating)

    def most_positive_user(self):
        av_rating = 0
        user = ""
        for i in self.users.values():
            if i.get_average_rating() > av_rating:
                av_rating = i.get_average_rating()
                user = i.__repr__()
        return "{} - {}".format(user, av_rating)
