from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def terms(request):
    return render(request,'terms.html')
def privacy(request):
    return render(request,'policy.html')

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)