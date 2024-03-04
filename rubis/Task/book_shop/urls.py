from django.urls import path
from book_shop.views import Book, Review

urlpatterns = [
    path('book/', Book.as_view()),
    path('review/', Review.as_view()),
]