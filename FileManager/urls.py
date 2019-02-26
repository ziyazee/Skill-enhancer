
from django.conf.urls import url
from FileManager import views
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name='FileManager'

urlpatterns = [
    url(r'FileManager/home/',views.home,name='home'),
    url(r'FileManager/(?P<year>[\f\w-]+)/$',views.subjects,name='subjects'),
    url(r'FileManager/files/(?P<categorie>[\f\w-]+)/$',views.files,name='files'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
