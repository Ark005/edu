from django.http import HttpResponse
from django.shortcuts import render

def robot_view(request):
    return render(request, 'robot.html', content_type='text/plain')

