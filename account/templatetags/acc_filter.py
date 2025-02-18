from django import template

register = template.Library()

@register.filter
def has_perm(user, perm_codename):
    """Custom template filter to check user permissions."""
    return user.has_permission(perm_codename)
@register.filter
def has_role(user, role):
    return user.has_role(role)