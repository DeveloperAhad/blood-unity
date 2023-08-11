import re

from django.shortcuts import redirect


def phone_or_email_validator(value):
    phone_pattern = r'^(011|015|016|018|017|013)\d{8}$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(phone_pattern, value):
        return 'phone'
    elif re.match(email_pattern, value):
        return 'email'
    else:
        return False



# Create your views here.
def unauthenticated_user(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        else:
            return func(request, *args, **kwargs)
    return wrapper