from django.urls import path
from .views import SignInView, logout_view, AddTeacherView, TeacherListView, TeacherDetailsView, AddStudentView, StudentListView, StudentDetailsView, StudentListByClassView, StudentListByNameView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('teacher/add/', AddTeacherView.as_view(), name='teacher_add'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<str:pk>/', TeacherDetailsView.as_view(), name='teacher_detail'),
    path('student/add/', AddStudentView.as_view(), name='student_add'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('student_details', StudentDetailsView.as_view(), name='student_details'),
    path('student_by_class/', StudentListByClassView.as_view(), name='student_by_class'),
    path('student_by_name/', StudentListByNameView.as_view(), name='student_by_name'),
]
