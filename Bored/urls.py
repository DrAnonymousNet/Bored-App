
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Bore.views import Home, NumberFormView, ActivityFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name = "index"),
    path("number/", NumberFormView, name= "number-form"),
    path("activity/", ActivityFormView, name="activity-form" )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
