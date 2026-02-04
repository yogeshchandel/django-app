from django.test import TestCase
from django.utils import timezone
from datetime import date
from author.models import Author
from .models import Book


class BookModelTest(TestCase):
    """Test cases for the Book model"""

    def setUp(self):
        """Set up test data"""
        self.author = Author.objects.create(
            name="Test Author",
            bio="Test bio",
            email="testauthor@example.com"
        )
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            published_date=date(2024, 1, 1),
            isbn_number="9781234567890"
        )

    def test_book_creation(self):
        """Test that a book can be created"""
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, self.author)
        self.assertEqual(self.book.isbn_number, "9781234567890")
        self.assertIsInstance(self.book, Book)

    def test_book_str_method(self):
        """Test the string representation of a book"""
        self.assertEqual(str(self.book), "Test Book")

    def test_book_author_relationship(self):
        """Test the foreign key relationship with Author"""
        self.assertEqual(self.book.author.name, "Test Author")
        self.assertEqual(self.book.author.email, "testauthor@example.com")

    def test_isbn_uniqueness(self):
        """Test that ISBN numbers must be unique"""
        with self.assertRaises(Exception):
            Book.objects.create(
                title="Another Book",
                author=self.author,
                published_date=date(2024, 2, 1),
                isbn_number="9781234567890"  # Duplicate ISBN
            )

    def test_book_fields(self):
        """Test that all required fields are present"""
        self.assertTrue(hasattr(self.book, 'title'))
        self.assertTrue(hasattr(self.book, 'author'))
        self.assertTrue(hasattr(self.book, 'published_date'))
        self.assertTrue(hasattr(self.book, 'isbn_number'))

    def test_cascade_delete(self):
        """Test that deleting an author deletes associated books"""
        book_id = self.book.id
        self.author.delete()
        self.assertFalse(Book.objects.filter(id=book_id).exists())


class AuthorModelTest(TestCase):
    """Test cases for the Author model"""

    def setUp(self):
        """Set up test data"""
        self.author = Author.objects.create(
            name="John Doe",
            bio="A test author",
            email="johndoe@example.com"
        )

    def test_author_creation(self):
        """Test that an author can be created"""
        self.assertEqual(self.author.name, "John Doe")
        self.assertEqual(self.author.bio, "A test author")
        self.assertEqual(self.author.email, "johndoe@example.com")

    def test_author_str_method(self):
        """Test the string representation of an author"""
        self.assertEqual(str(self.author), "John Doe")

    def test_email_uniqueness(self):
        """Test that email addresses must be unique"""
        with self.assertRaises(Exception):
            Author.objects.create(
                name="Jane Doe",
                bio="Another author",
                email="johndoe@example.com"  # Duplicate email
            )

