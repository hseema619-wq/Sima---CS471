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
    path('search', views.search, name='search'),#lab6 task1
    path('simple/query', views.simple_query, name='simple_query'),#lab7 task3
    path('complex/query', views.complex_query, name='complex_query'),#lab7 task4
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7, name='task7'),
    path('lab9/task1/', views.lab9_task1),
    path('lab9/task2/', views.lab9_task2),
    path('lab9/task3/', views.lab9_task3),
    path('lab9/task4/', views.lab9_task4),
    path('lab9/task5/', views.lab9_task5),
    path('lab9/task6/', views.lab9_task6),
]