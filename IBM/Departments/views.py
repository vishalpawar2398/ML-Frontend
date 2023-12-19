from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def hr(r):
    return render(r,'departments/HR.html')

def admin(r):
    return render(r,'departments/admin.html')


def finance(r):
    return render(r,'departments/Finance.html')


def it(r):
    return render(r,'departments/IT.html')



