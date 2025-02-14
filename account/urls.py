from django.urls import path
from .views import SignInView, logout_view, AddTeacherView, TeacherListView, TeacherDetailsView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('teacher/add/', AddTeacherView.as_view(), name='teacher_add'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<str:pk>/', TeacherDetailsView.as_view(), name='teacher_detail'),
    # path('student/add/', AddStudentView.as_view(), name='student_add'),
]
