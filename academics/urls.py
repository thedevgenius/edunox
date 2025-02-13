from django.urls import path
from .views import GetSectionView

urlpatterns = [
    path('get-section-by-class/', GetSectionView.as_view(), name='get_section'),
    
]
