from django.contrib import admin
from django.urls import path, include
from crudgro_web.views import test_response
from django.conf import settings
from django.conf.urls.static import static
from crudgro_web.views import all_articles

urlpatterns = [
    path('', all_articles),
    path('admin/', admin.site.urls),
    path('test/', test_response),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
