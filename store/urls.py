from django.urls import path, include  # this statement lets us define URL routes 
from .import views #imports the views.py


urlpatterns = [
    path('', views.home_view, name='home'),             # new homepage
    path('products/', views.product_view, name='product'),  # products page
    path('accounts/login/', views.login_view, name='login'),  # custom login page
    path('accounts/logout/', views.logout_view, name='logout'),  # custom logout page
    path('signup/', views.signup_view, name='signup'),  # custom signup page
]