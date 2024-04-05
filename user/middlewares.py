from django.shortcuts import redirect


def auth(view_function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapper
