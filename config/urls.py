
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from llm.views import upload_file

urlpatterns = [
    path("",upload_file, name="upload_file"),
    path('admin/', admin.site.urls),
    path('', include('llm.urls',namespace='llm')),
    path('register/',include("register.urls",namespace="register")),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)