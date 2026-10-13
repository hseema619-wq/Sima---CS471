from django.urls import path
from . import views
urlpatterns = [
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),

    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path("html5/links", views.links, name="links"),#lab5 task1
    path("html5/text/formatting", views.formatting, name="formatting"),#lab5 task2
    path('html5/listing', views.listing, name='listing'),#lab5 task3
    path('html5/tables', views.tables, name='tables'),#lab5 task4
]