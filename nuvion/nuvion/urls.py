# yourproject/urls.py
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from nuvion import views
from django.conf import settings
from django.conf.urls.static import static

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('termsandcondition/',views.terms),
    path('privacypolicy/',views.privacy),
    path('workwithus/', include('workwithus.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
