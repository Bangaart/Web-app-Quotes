from django.urls import path

from authors import views

app_name = 'authors'
urlpatterns = [
    path('add/', views.add, name='add'),
    path('details/', views.AuthorsListView.as_view(), name='details'),
    path('<int:pk>/', views.AuthorDetailView.as_view(), name='authorPage'),
]
