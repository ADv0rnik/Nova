from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django_email_verification import urls as email_urls

from courses.views import index


urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('', include(email_urls)),
    path('tinymce/', include('tinymce.urls')),
    path('courses/', include('courses.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
