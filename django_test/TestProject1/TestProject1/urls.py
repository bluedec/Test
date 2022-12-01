from django.contrib import admin
from django.urls import include, path

from .views import saludin

urlpatterns = [
    path('polls/', include('Polls.urls')),
    path('admin/', admin.site.urls),
    path('saludin/', saludin)
]
