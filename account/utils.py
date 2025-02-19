from academics.models import Grade
from .models import User

def student_filter(class_id, name):
    if class_id and name:
        grade = Grade.objects.get(id=class_id)
        students = User.objects.filter(type='ST', student_profile__grade=grade, first_name__startswith=name).select_related('student_profile').order_by('student_profile__total_roll')
    elif class_id and not name:
        grade = Grade.objects.get(id=class_id)
        students = User.objects.filter(type='ST', student_profile__grade=grade).select_related('student_profile').order_by('student_profile__total_roll')
    elif name and not class_id:
        students = User.objects.filter(type='ST', first_name__startswith=name).select_related('student_profile').order_by('student_profile__total_roll')
    else:
        students = User.objects.filter(type='ST').select_related('student_profile').order_by('first_name')
    return students