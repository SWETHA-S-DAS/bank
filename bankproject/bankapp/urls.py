from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name='bankapp'
urlpatterns = [
    path('', views.demo, name='demo'),
    path('district/' ,views.demo,name='district')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
