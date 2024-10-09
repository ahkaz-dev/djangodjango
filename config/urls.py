from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # home path
    path('', include('catalog.urls')),
    path('contacts/', include('contacts.urls')),

    path('admin/', admin.site.urls),
]