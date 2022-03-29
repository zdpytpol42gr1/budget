from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('hi/', views.hi_page_view, name='hi_page'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
