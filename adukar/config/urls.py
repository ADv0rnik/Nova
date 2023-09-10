from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from ..courses.views import index


urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
