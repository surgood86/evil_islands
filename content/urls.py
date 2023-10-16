from django.urls import path
from . import views
urlpatterns = [
    path('', views.ContentListViews.as_view(), name='content'),
    path('', views.base, name='base'),
    path('services/', views.services, name='services'),
    path('projects-2/', views.projects_2, name='projects-2'),
    path('projects-3/', views.projects_3, name='projects-3'),
    path('project-details/', views.project_details, name='project-details'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('our-team/', views.our_team, name='our-team'),
    path('archives/', views.archives, name='archives'),
    path('grids/', views.grids, name='grids'),
    path('404/', views.error_404, name='404'),
    path('contact/', views.contact, name='contact'),
]

