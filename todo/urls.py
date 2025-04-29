from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.todo_create,name='todo_create'),
    path('',views.todo_list,name='todo_list'),
    path('update/<str:pk>',views.todo_update,name='todo_update'),
    path('delete/<str:pk>',views.todo_delete,name='todo_delete'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')
]