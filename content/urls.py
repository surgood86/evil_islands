from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContentListViews.as_view(), name='content_list'),
    path('', views.base, name='base'),
    path('project-detail/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('our-team/', views.our_team, name='our-team'),
    #path('archives/', views.archives, name='archives'),
    #path('grids/', views.grids, name='grids'),
    path('contact/', views.contact, name='contact'),
]
