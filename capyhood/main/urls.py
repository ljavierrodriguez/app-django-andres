from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('task/add', views.save_task, name="save_task"),
    path('task/<int:id>/delete', views.delete_task, name="delete_task"),
    path('task/<int:id>/complete', views.complete_task, name="complete_task"),
]
