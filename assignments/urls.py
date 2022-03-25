from unicodedata import name
from django.urls import path
from . import views


app_name = 'assignments'

urlpatterns = [
    path('', views.AssignmentsListView.as_view(), name='all'),
    path('<int:pk>/detail', views.AssignmentsDetailView.as_view(), name='assignments_detail'),
    path('create/', views.AssignmentsCreateView.as_view(), name='assignments_create'),
    path('<int:pk>/update', views.AssignmentsUpdateView.as_view(), name='assignments_update'),
    path('<int:pk>/delete', views.AssignmentsDeleteView.as_view(), name='assignments_delete'),
    
]
