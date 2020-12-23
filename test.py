from django.contrib import auth
from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user_obj = authenticate(username=username, password=password)
    if user_obj:
        login(request, user_obj)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...