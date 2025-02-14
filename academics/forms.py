# from django import forms
# from .models import Subject
# from academics.models import Class

# class AddSubjectForm(forms.ModelForm):
#     name = forms.CharField(label='Subject Name' ,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. Mathematics'}))
#     class_obj = forms.ModelChoiceField(queryset=Class.objects.all(), label='Class Name', widget=forms.Select(attrs={'class': 'select'}))

#     class Meta:
#         model = Subject
#         fields = ['name', 'code', 'class_obj']