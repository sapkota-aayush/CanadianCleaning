from django.contrib import admin
from django.urls import path
from my_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),   # admin site
    path('home/', home, name='home'),  # your home view
]
