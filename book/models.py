from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=100, blank=True, null=True)
    borrowed_at = models.DateTimeField(blank=True, null=True)

    def borrow(self, borrower_name):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrower_name = borrower_name
            self.borrowed_at = timezone.now()
            self.save()

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrower_name = None
            self.borrowed_at = None
            self.save()

    def __str__(self):
        return self.title
