from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Book
from django.http import HttpResponse

# List all available books
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# View details of a book
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

# Borrow a book
class BorrowBookView(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if not book.is_borrowed:
            borrower_name = request.POST.get('borrower_name')
            book.borrow(borrower_name)
            return redirect('book_detail', pk=pk)
        return HttpResponse("This book is already borrowed!", status=400)

# Return a book
class ReturnBookView(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.is_borrowed:
            book.return_book()
            return redirect('book_detail', pk=pk)
        return HttpResponse("This book is not borrowed!", status=400)
