from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"backend/task/",include("task.urls")),
    path(r"restapi/",include("rest_framework.urls"))
]
