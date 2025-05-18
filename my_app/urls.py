from django.contrib import admin
from django.urls import path
from my_app.views import home, about, service

urlpatterns = [
    path('admin/', admin.site.urls),   # admin site
    path('home/', home, name='home'),  # your home view
    path('about/', about, name='about'),  # your about view
    path('service/', service, name='service'),  # your service view
]
