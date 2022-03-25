from unicodedata import name
from django.urls import path
from . import views


app_name = 'quizes'

urlpatterns = [
    path('', views.QuizesListView.as_view(), name='all'),
    path('<int:pk>/detail', views.QuizesDetailView.as_view(), name='quizes_detail'),
    path('create/', views.QuizesCreateView.as_view(), name='quizes_create'),
    path('<int:pk>/update', views.QuizesUpdateView.as_view(), name='quizes_update'),
    path('<int:pk>/delete', views.QuizesDeleteView.as_view(), name='quizes_delete'),
    
]
