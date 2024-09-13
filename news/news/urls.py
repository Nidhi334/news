
from django.contrib import admin
from django.urls import path
from newsblog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="homepage"),
    path("search/",search, name="search"),
    path("<str:category>/", index, name="filter"),
    path("viewpost/<int:postid>", viewpost, name="viewpost"),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
