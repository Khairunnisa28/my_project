
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.student_list, name='student_list'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
]

