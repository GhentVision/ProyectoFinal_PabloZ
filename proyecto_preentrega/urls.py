from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from proyecto_preentrega.views import inicio

urlpatterns = [
    path("", inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path("plataforma/", include("control_estudios.urls")),
    path("blog/",  include("blog_learning.urls")),
    path("perfiles/", include("perfiles.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
