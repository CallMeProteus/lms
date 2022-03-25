from unicodedata import name
from django.urls import path
from . import views


app_name = 'content'

urlpatterns = [
    path('', views.ContentListView.as_view(), name='all'),
    path('content/<int:pk>/detail', views.ContentDetailView.as_view(), name='content_detail'),
    path('content/create/', views.ContentCreateView.as_view(), name='content_create'),
    path('content/<int:pk>/update', views.ContentUpdateView.as_view(), name='content_update'),
    path('content/<int:pk>/delete', views.ContentDeleteView.as_view(), name='content_delete'),
    
]
