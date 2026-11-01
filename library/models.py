from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrowed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.borrower_name} - {self.book.title}"
