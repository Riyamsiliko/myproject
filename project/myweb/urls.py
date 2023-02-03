from django.urls import path
from . import views

app_name="myweb"
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('logout',views.logout,name='logout'),
    path('studentlist/', views.student_list, name='student_list'),
    path('<int:student_id>/', views.single_student, name='single_student'),
    path('registration/', views.student_registration, name='student_registration'),
    path('edit/<int:pk>', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>', views.delete_student, name='delete_student'),

]

