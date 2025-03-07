from django.urls import path
from .views import ClassListView, ClassDetailView, AddAttendanceView

urlpatterns = [
    # path('subjects/', SubjectListView.as_view(), name='subject_list'),
    # path('subject/add/', AddSubjectView.as_view(), name='subject_add'),
    path('classes/', ClassListView.as_view(), name='class_list'),
    path('class/<int:pk>/', ClassDetailView.as_view(), name='class_details'),
    path('class/<int:pk>/attendance/add/', AddAttendanceView.as_view(), name='attendance_add'),
]


