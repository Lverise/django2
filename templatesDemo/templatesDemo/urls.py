from django.contrib import admin
from django.urls import path
from templatesApp.views import renderTemplate, renderTemplate2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('render/', renderTemplate),
    path('render2/', renderTemplate2)
]
