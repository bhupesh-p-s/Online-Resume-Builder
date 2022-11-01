from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('template/', views.testing,name='template'),
    path('resume/', views.home, name="home"),
    path('',views.testing,name="template")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)