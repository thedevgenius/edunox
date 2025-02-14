from django.shortcuts import render
from django.http import JsonResponse
from .models import Grade
from django.views.generic import View, CreateView, TemplateView

# Create your views here.

# class GetSectionView(View):
#     def get(self, request, *args, **kwargs):
#         id = request.GET.get('class_id')
#         class_obj = Class.objects.get(id=id)
#         sections = Section.objects.filter(class_obj=Class.objects.get(id=id))
#         sections_list = list(sections.values('id', 'name'))
#         return JsonResponse({'success': True, 'sections': sections_list})
    
class ClassListView(TemplateView):
    template_name = 'academics/class_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        grades = Grade.objects.all()
        context['grades'] = grades
        return context


# class SubjectListView(TemplateView):
#     template_name = 'academics/subject_list.html'

# class AddSubjectView(CreateView):
#     model = Subject
#     form_class = AddSubjectForm
#     template_name = 'academics/subject_add.html'

    