# The base class for all books.
class Book:
    """A class to represent a generic book."""

    # Constructor to initialize a book with its basic attributes.
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    # Method to print the book's information.
    def display_info(self):
        """Prints out the book's key information."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")

    # Method to simulate reading the book.
    def read(self):
        """Simulates reading the book."""
        print(f"You are now reading '{self.title}' by {self.author}.")

# A subclass for non-fiction books that inherits from Book.
class NonFictionBook(Book):
    """A subclass for non-fiction books, with a specific core concept."""

    # Constructor for the subclass.
    # It calls the parent's constructor and adds a new attribute.
    def __init__(self, title, author, genre, pages, core_concept):
        super().__init__(title, author, genre, pages)
        self.core_concept = core_concept

    # Overridden method to include the core concept.
    def display_info(self):
        """Prints out the non-fiction book's information, including its core concept."""
        super().display_info()
        print(f"Core Concept: {self.core_concept}")

    # New method specific to this subclass.
    def apply_concept(self):
        """Demonstrates applying the book's core concept."""
        print(f"You are now applying the '{self.core_concept}' concept from '{self.title}'.")


# --- Example Usage ---

# Creating an instance of the parent class.
print("--- Creating a standard Fiction Book ---")
mockingbird = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 281)
mockingbird.display_info()
mockingbird.read()
print("-" * 30)

# Creating an instance of the subclass.
print("\n--- Creating the 'Good to Great' Non-Fiction Book ---")
good_to_great = NonFictionBook("Good to Great", "Jim Collins", "Non-Fiction", 300, "The Hedgehog Concept")
good_to_great.display_info()
good_to_great.read()
good_to_great.apply_concept()
print("-" * 30)
