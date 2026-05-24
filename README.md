#  Library Management System

##  Project Description

This project is a library management system developed in Python as part of group assignment 1 for the Advanced Programming course. It manages books, members, and calculates library statistics.

##  Assignment Goals

This program meets all assignment requirements:

###  Part 1 - Fix the Basics
-  Correct use of the 4 data types: `str`, `int`, `float`, `bool`
-  Correct boolean handling using `.lower() == "yes"` instead of `bool(input())`
-  More than 10 `input()` calls with appropriate conversion
-  3+ meaningful arithmetic expressions
-  Input validation with `while` loops and `try/except`
-  Use of f-strings for all output
-  Clear summary screen at the end

###  Part 2 - Inheritance
-  Parent class: `Document`
-  Child class: `Book` inherits from `Document`
-  Parent constructor called with ` super().__init__()`
-  Added specific attributes: `num_pages`, `isbn`
-  Added specific methods: `is_long()`, `full_description`

###  Part 3 - Magic Methods (Research)
-  `__str__()` : Custom object display
-  `__len__()` : Returns the number of pages of a book
-  `__eq__()` : Compares two documents by their code

###  Part 4 - Decorators (Research)
-  `@staticmethod` : `validate_year()` method in `Document`
-  `@classmethod` : `get_total_members()` method in `Member`
-  `@property` : `full_description` property in `Book`

##  Code Structure

### Main Classes

#### 1. `Document` (Parent Class)
Represents a generic document in the library.

**Attributes:**
- `title` : Document title
- `author` : Document author
- `year` : Publication year
- `code` : Unique identification code
- `borrowed` : Borrowed status (boolean)

**Methods:**
- `borrow()` : Marks the document as borrowed
- `return_item()` : Marks the document as returned
- `validate_year()` : Static method to validate a year

**Magic Methods:**
- `__str__()` : Formatted document display
- `__eq__()` : Compare documents by code

#### 2. `Book` (Child Class)
Inherits from `Document` and represents a book specifically.

**Additional Attributes:**
- `num_pages` : Number of pages
- `isbn` : ISBN number

**Additional Methods:**
- `is_long()` : Determines if the book is long (>300 pages)
- `full_description` : Property returning a full description

**Magic Methods:**
- `__str__()` : Formatted book display (override)
- `__len__()` : Returns the number of pages

#### 3. `Member`
Represents a library member.

**Attributes:**
- `last_name` : Member last name
- `first_name` : Member first name
- `age` : Member age
- `member_number` : Unique number
- `borrowed_books` : List of borrowed books

**Methods:**
- `can_borrow()` : Checks if the member can borrow more books
- `get_total_members()` : Class method returning total members

##  How to Run the Program

### Prerequisites
- Python 3.6 or higher installed on your machine

### Instructions

1. **Clone the GitHub repository**
```bash
git clone https://github.com/your-username/library-management.git
cd library-management
```

2. **Run the program**
```bash
python bibliotheque.py
```

3. **Follow the on-screen instructions**
   - Enter library information
   - Add books
   - Register members
   - View statistics and the summary

##  Example Usage

```
==============================================================
         LIBRARY MANAGEMENT SYSTEM 
==============================================================

Welcome to the library management system!
We are going to configure your library.

  Library name : Central Library
  City : Ouagadougou
 Foundation year : 1995
 Monthly budget (FCFA) : 500000.50
 Number of floors : 3
 Total area (m²) : 1200.75
  Open on Sunday? (yes/no) : yes
 Has a café? (yes/no) : yes

 Library 'Central Library' configured!
    Located in Ouagadougou
    Age : 31 years
    Area per floor : 400.25 m²

How many books do you want to add? 2
...
```

##  Key Concepts Demonstrated

### Input Validation
The program uses robust validation functions:
- `read_text()` : Validates that input is not empty
- `read_int()` : Validates integers with min/max
- `read_float()` : Validates decimal numbers
- `read_bool()` : Correctly validates booleans

### Arithmetic Expressions
1. **Borrow percentage** : `(borrowed_books / total_books) * 100`
2. **Average pages** : `total_pages / total_books`
3. **Books/members ratio** : `total_books / total_members`

### Magic Methods Used
- `__str__` : For readable object display
- `__len__` : To get length (number of pages)
- `__eq__` : To compare objects

### Decorators Used
- `@staticmethod` : For methods that do not depend on the instance
- `@classmethod` : For accessing class variables
- `@property` : For creating computed attributes

##  Future Improvements

- Save data to a JSON file
- Add a book search feature
- Implement a reservation system
- Create a graphical user interface (GUI)
- Add a late fee penalty system

##  Author

**[Your Name]**
- Course : Advanced Programming
- Assignment : Group 1
- Date : May 2026

##  License

This project is developed for educational purposes as part of the Advanced Programming course.

---

**Note** : This program was designed to demonstrate mastery of core Python concepts, inheritance, magic methods, and decorators, in accordance with the assignment requirements.
