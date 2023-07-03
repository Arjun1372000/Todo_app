from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

# app name and urlpatterns path name set for easier access to the html pages
app_name = 'todo'

# first argument of path along with parent urlpatterns is what will be shown as endpoints in the web-app links
urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.index, name='homepage'),
    path('signup/', views.signup, name='signup'),

    # used the default views available for Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='todo/logout.html'), name='logout'),
]
