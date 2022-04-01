from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('hi/', views.hi_page_view, name='hi_page'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_user/<str:username>/', views.del_user, name='del_user'),
    path('user_list/', views.user_list_view, name='user_list'),
    path('change_password/', views.change_password_by_user, name='change_password'),
]
