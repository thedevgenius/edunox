from django.urls import path
from .views import ClassListView

urlpatterns = [
    # path('get-section-by-class/', GetSectionView.as_view(), name='get_section'),
    # path('subjects/', SubjectListView.as_view(), name='subject_list'),
    # path('subject/add/', AddSubjectView.as_view(), name='subject_add'),
    path('grades/', ClassListView.as_view(), name='class_list'),
]
