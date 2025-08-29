Overview
This library provides a set of Python classes for representing different types of books. It includes a base Book class and specialized subclasses for different book categories, with methods for displaying information, reading simulation, and book-specific actions.

Classes
Book (Base Class)
The foundational class that represents a generic book with common attributes.

Attributes:

title (str): The title of the book

author (str): The author of the book

genre (str): The genre of the book

pages (int): The number of pages in the book

Methods:

display_info(): Prints the book's key information

read(): Simulates reading the book

NonFictionBook (Subclass)
Extends the Book class to represent non-fiction books with specialized concepts.

Additional Attribute:

core_concept (str): The central concept or idea of the non-fiction book

Methods:

display_info(): Overridden to include the core concept

apply_concept(): Demonstrates applying the book's core concept

Vehicle (Base Class - Bonus)
A bonus class demonstrating polymorphism with different vehicle types.

Attributes:

make (str): The manufacturer of the vehicle

model (str): The model of the vehicle

Methods:

move(): A generic method for movement

Car (Subclass)
Extends Vehicle to represent cars with specific attributes.

Additional Attribute:

fuel_type (str): The type of fuel the car uses

Methods:

move(): Overridden to describe car-specific movement

Plane (Subclass)
Extends Vehicle to represent planes with specific attributes.

Additional Attribute:

max_altitude (int): The maximum altitude the plane can reach

Methods:

move(): Overridden to describe plane-specific movement
