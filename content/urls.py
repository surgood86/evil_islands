from django.urls import path

from content import views

urlpatterns = [
    path('', views.ContentListViews.as_view(), name='content')
]
