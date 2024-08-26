from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    # path('<homepage>', views.dynamic_homepage)
    path('details/<int:todo_id>', views.detail, name='details'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>',views.update,name='update'),
    path('create/', views.create, name='create'),

]
