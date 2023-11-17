from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]