from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('testimonial/', views.submit_testimonial, name='submit_testimonial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)