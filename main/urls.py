from django.urls import path, include, register_converter
from django.conf.urls.static import static
from main import views
from webapp import settings


urlpatterns = [
    path('', views.head, name='home'),
    path('about/', views.about, name='about'),
    path('model/', views.MakeCalculations.as_view(), name='model'),
    path('model/result', views.result, name='result'),
    path('download/result/', views.download_pdf, name='download_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
