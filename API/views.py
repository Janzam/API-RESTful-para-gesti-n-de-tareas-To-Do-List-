from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'home.html')

from django.shortcuts import redirect

def redirect_to_tasks(request):
    return redirect('/api/tasks')