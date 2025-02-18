from django.urls import path
from .views import HomeView, DashboardView, get_student_by_gender

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('get-student-by-gender/', get_student_by_gender, name='get_student_by_gender'),
]
