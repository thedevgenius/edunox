from django.shortcuts import render
from django.http import JsonResponse
from .models import Class, Section
from django.views.generic import View
# Create your views here.

class GetSectionView(View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('class_id')
        class_obj = Class.objects.get(id=id)
        sections = Section.objects.filter(class_obj=Class.objects.get(id=id))
        sections_list = list(sections.values('id', 'name'))
        return JsonResponse({'success': True, 'sections': sections_list})
        