from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.user_signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('index2', views.index2, name='index2'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
]