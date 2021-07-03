from django.urls import path, include
from . import views
app_name='book'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name="book-detail")

]
