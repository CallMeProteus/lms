from unicodedata import name
from django.urls import path
from . import views


app_name = 'announcements'

urlpatterns = [
    path('', views.AnnouncementsListView.as_view(), name='all'),
    path('<int:pk>/detail', views.AnnouncementsDetailView.as_view(), name='announcements_detail'),
    path('create/', views.AnnouncementsCreateView.as_view(), name='announcements_create'),
    path('<int:pk>/update', views.AnnouncementsUpdateView.as_view(), name='announcements_update'),
    path('<int:pk>/delete', views.AnnouncementsDeleteView.as_view(), name='announcements_delete'),
    
]