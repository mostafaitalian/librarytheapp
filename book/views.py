from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
# Create your views here.
from .models import Book


class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['books'] = Book.objects.all()
        return ctx
    template_name = 'home.html'
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.all()

    template_name= 'book/book_list.html'
class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

