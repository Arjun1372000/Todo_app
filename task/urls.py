from django.urls import path

from . import views

# app name and urlpatterns path name set for easier access to the html pages
app_name = 'task'

# first argument of path along with parent urlpatterns is what will be shown as endpoints in the web-app links
urlpatterns = [
    path('view/', views.view_task, name='view'),
    path('completed/', views.completed_task, name='completed'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
