from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Redirige directamente al área de tareas
@login_required
def home(request):
    return redirect('/api/tasks/')

# Verifica autenticación (puede usarse con fetch desde el frontend si lo necesitas)
@login_required
def check_authentication(request):
    return JsonResponse({
        'authenticated': True,
        'username': request.user.username
    })
