from django.contrib import admin
from django.urls import path, include
from main.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls', namespace="users")),
]

handler404 = page_not_found
