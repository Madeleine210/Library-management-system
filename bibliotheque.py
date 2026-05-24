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
