from django.urls import path
from .views import BookListView, BookDetailView, BorrowBookView, ReturnBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('<int:pk>/return/', ReturnBookView.as_view(), name='return_book'),
]
