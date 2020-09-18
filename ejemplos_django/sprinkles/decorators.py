from functools import wraps
from . import utils

def check_sprinkles(view_func):
    """Check if a user can add sprinkles"""
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        # Act on the request object with utils.can_sprinkle()
        request = utils.can_sprinkle(request)
        # Call the view function
        response = view_func(request, *args, **kwargs)
        # Return the HttpResponse object
        return response
    return new_view_func