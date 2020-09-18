from django.core.exceptions import PermissionDenied

def check_sprinkle_rights(request):
    if request.user.can_sprinkle or request.user.is_staff:
        request.can_sprinkle = True
        return request
    # Return a HTTP 403 back to the user
    raise PermissionDenied