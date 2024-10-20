from django.contrib import admin
from django.urls import include, path

from catalog import views

urlpatterns = [
    # home path
    path('', include('catalog.urls')),
    path('books/', views.book, name='home.html'),

    path('contacts/', include('contacts.urls')),

    path('admin/', admin.site.urls),
]