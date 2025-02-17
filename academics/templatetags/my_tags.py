from django import template
from academics.models import Subject, Schedule, Grade
from account.models import User

register = template.Library()

@register.filter(name='period')
def period(day, args):
    try:
        # Ensure args is a string
        if not isinstance(args, str):
            args = str(args)

        # Validate if it contains a comma
        if ',' not in args:
            return "Invalid arguments"

        grade_id, p_id = args.split(',')
        
        # Convert values to integers
        grade_id = int(grade_id.strip())
        p_id = int(p_id.strip())

        schedule = Schedule.objects.get(day=day, grade_id=grade_id, period=p_id)
        return schedule.subject  # Ensure returning a string
    except Schedule.DoesNotExist:
        return "Schedule Does Not Exist"