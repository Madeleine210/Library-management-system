"""
Library Management System
Group Assignment 1 - Advanced Programming
"""

# Part 2: Inheritance - Parent Class
class Document:
    """Parent class representing a generic document in the library."""

    def __init__(self, title, author, year, code):
        self.title = title
        self.author = author
        self.year = year
        self.code = code
        self.borrowed = False

    # Part 3: Magic Method __str__
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {status}"

    # Part 3: Magic Method __eq__
    def __eq__(self, other):
        """Compare two documents by their unique code."""
        if isinstance(other, Document):
            return self.code == other.code
        return False

    def borrow(self):
        """Mark the document as borrowed."""
        if not self.borrowed:
            self.borrowed = True
            return True
        return False

    def return_item(self):
        """Mark the document as returned."""
        if self.borrowed:
            self.borrowed = False
            return True
        return False

    # Part 4: @staticmethod decorator
    @staticmethod
    def validate_year(year):
        """Validate that a year is reasonable for a document."""
        current_year = 2026
        return 1000 <= year <= current_year


# Part 2: Inheritance - Child Class
class Book(Document):
    """Child class representing a book (inherits from Document)."""

    def __init__(self, title, author, year, code, num_pages, isbn):
        # Call the parent constructor with super()
        super().__init__(title, author, year, code)
        # New attributes specific to books
        self.num_pages = num_pages
        self.isbn = isbn

    # Part 3: Magic Method __str__ (override)
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {self.num_pages} pages - ISBN: {self.isbn} - {status}"

    # Part 3: Magic Method __len__
    def __len__(self):
        """Return the number of pages in the book."""
        return self.num_pages

    # New method specific to books
    def is_long(self):
        """Determine if the book is considered long."""
        return self.num_pages > 300

    # Part 4: @property decorator
    @property
    def full_description(self):
        """Return a complete description of the book."""
        length = "long" if self.is_long() else "short"
        return f"{self.title} is a {length} book of {self.num_pages} pages written by {self.author}."


# Part 4: @classmethod decorator
class Member:
    """Class representing a library member."""

    # Class variable to count members
    total_members = 0

    def __init__(self, last_name, first_name, age, member_number):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.member_number = member_number
        self.borrowed_books = []
        Member.total_members += 1

    # Part 3: Magic Method __str__
    def __str__(self):
        return f" {self.first_name} {self.last_name} (#{self.member_number}) - {len(self.borrowed_books)} book(s) borrowed"

    # Part 4: @classmethod decorator
    @classmethod
    def get_total_members(cls):
        """Return the total number of registered members."""
        return cls.total_members

    def can_borrow(self, max_books=3):
        """Check if the member can borrow more books."""
        return len(self.borrowed_books) < max_books


def read_text(message):
    """Part 1: Text input validation with a while loop."""
    while True:
        text = input(message).strip()
        if text:
            return text
        print(" Input cannot be empty. Please try again.")


def read_int(message, min_val=None, max_val=None):
    """Part 1: Integer input validation with try/except."""
    while True:
        try:
            value = int(input(message))
            if min_val is not None and value < min_val:
                print(f" The value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f" The value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print(" Please enter a valid integer.")


def read_float(message, min_val=None):
    """Part 1: Float input validation with try/except."""
    while True:
        try:
            value = float(input(message))
            if min_val is not None and value < min_val:
                print(f" The value must be at least {min_val}.")
                continue
            return value
        except ValueError:
            print(" Please enter a valid decimal number.")


def read_bool(message):
    """Part 1: Correct boolean input validation."""
    while True:
        response = input(message).strip().lower()
        if response in ("yes", "y"):
            return True
        if response in ("no", "n"):
            return False
        print(" Please enter 'yes' or 'no'.")


def show_banner():
    """Display the system banner."""
    print("\n" + "=" * 60)
    print(" LIBRARY MANAGEMENT SYSTEM ".center(60))
    print("=" * 60 + "\n")


def create_book():
    """Create a new book with full validation."""
    print("\n---  ADDING A NEW BOOK ---\n")

    # Part 1: At least 10 input() calls with appropriate conversion
    title = read_text(" Book title: ")
    author = read_text("  Author: ")

    # Validate the year with a static method
    while True:
        year = read_int(" Publication year: ", 1000, 2026)
        if Document.validate_year(year):
            break
        print(" Invalid year.")

    code = read_text(" Book code (e.g. LIV001): ")
    num_pages = read_int(" Number of pages: ", 1, 10000)
    isbn = read_text(" ISBN: ")

    book = Book(title, author, year, code, num_pages, isbn)
    print(f"\n Book created successfully!")
    print(f"   {book}")
    print(f"   {book.full_description}")

    return book


def create_member():
    """Create a new member with full validation."""
    print("\n---  REGISTERING A NEW MEMBER ---\n")

    last_name = read_text(" Last name: ")
    first_name = read_text(" First name: ")
    age = read_int(" Age: ", 1, 120)
    member_number = read_text(" Member number (e.g. MEM001): ")

    member = Member(last_name, first_name, age, member_number)
    print(f"\n Member registered successfully!")
    print(f"   {member}")

    return member


def calculate_statistics(books, members):
    """Part 1: At least 3 meaningful arithmetic expressions."""
    print("\n" + "=" * 60)
    print(" LIBRARY STATISTICS".center(60))
    print("=" * 60)

    # Arithmetic expression 1: Calculate borrowed books percentage
    total_books = len(books)
    borrowed_books = sum(1 for book in books if book.borrowed)
    if total_books > 0:
        borrow_percentage = (borrowed_books / total_books) * 100
    else:
        borrow_percentage = 0.0

    # Arithmetic expression 2: Calculate average pages per book
    total_pages = sum(len(book) for book in books)  # Uses __len__
    if total_books > 0:
        average_pages = total_pages / total_books
    else:
        average_pages = 0.0

    # Arithmetic expression 3: Calculate books/members ratio
    total_members = len(members)
    if total_members > 0:
        books_members_ratio = total_books / total_members
    else:
        books_members_ratio = 0.0

    # Part 1: Use f-strings for all output
    print(f"\n Total books: {total_books}")
    print(f" Borrowed books: {borrowed_books}")
    print(f" Available books: {total_books - borrowed_books}")
    print(f" Borrow percentage: {borrow_percentage:.2f}%")
    print(f"\n Total pages: {total_pages:,}")
    print(f" Average pages per book: {average_pages:.1f}")
    print(f"\n👥 Total members: {total_members}")
    print(f" Books/members ratio: {books_members_ratio:.2f}")

    # Use @classmethod
    print(f" Registered members (via @classmethod): {Member.get_total_members()}")

    print("=" * 60 + "\n")


def show_summary(books, members):
    """Part 1: Display a clear summary screen at the end."""
    print("\n" + "=" * 60)
    print(" FINAL SUMMARY".center(60))
    print("=" * 60 + "\n")

    print(" REGISTERED BOOKS:")
    print("-" * 60)
    if books:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
    else:
        print("No books registered.")

    print("\n REGISTERED MEMBERS:")
    print("-" * 60)
    if members:
        for i, member in enumerate(members, 1):
            print(f"{i}. {member}")
    else:
        print("No members registered.")

    print("\n" + "=" * 60)
    calculate_statistics(books, members)


def main_menu():
    """Main program function."""
    show_banner()

    books = []
    members = []

    # Part 1: At least 10 input() calls with appropriate conversion
    print("Welcome to the library management system!")
    print("We are going to configure your library.\n")

    # Input 1: Library name
    library_name = read_text(" Library name: ")

    # Input 2: City
    city = read_text(" City: ")

    # Input 3: Foundation year
    foundation_year = read_int(" Foundation year: ", 1000, 2026)

    # Input 4: Monthly budget (float)
    budget = read_float(" Monthly budget (FCFA): ", 0)

    # Input 5: Number of floors
    num_floors = read_int(" Number of floors: ", 1, 100)

    # Input 6: Total area (float)
    total_area = read_float(" Total area (m²): ", 0)

    # Input 7: Open on Sunday (bool)
    open_on_sunday = read_bool(" Open on Sunday? (yes/no): ")

    # Input 8: Has a café (bool)
    has_cafe = read_bool(" Has a café? (yes/no): ")

    # Calculation: Library age
    library_age = 2026 - foundation_year

    # Calculation: Area per floor
    area_per_floor = total_area / num_floors

    print(f"\n Library '{library_name}' configured!")
    print(f"    Located in {city}")
    print(f"    Age: {library_age} years")
    print(f"    Area per floor: {area_per_floor:.2f} m²")

    # Input 9 & 10: Number of books and members to add
    num_books = read_int("\n How many books do you want to add? ", 0, 100)

    for i in range(num_books):
        print(f"\n--- Book {i+1}/{num_books} ---")
        book = create_book()
        books.append(book)

    num_members = read_int("\n👥 How many members do you want to register? ", 0, 100)

    for i in range(num_members):
        print(f"\n--- Member {i+1}/{num_members} ---")
        member = create_member()
        members.append(member)

    # Demonstration of magic methods
    if len(books) >= 2:
        print("\n Demonstration of the magic method __eq__:")
        print(f"   {books[0].title} == {books[1].title} ? {books[0] == books[1]}")

    # Display final summary
    show_summary(books, members)

    # End message
    print("\n Thank you for using the library management system!")
    print(f" {library_name} in {city} is now operational!")

    if open_on_sunday:
        print(" Remember: we are open on Sunday!")

    if has_cafe:
        print(" Stop by the café for a reading break!")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main_menu()
