
from django.conf.urls import url
from CodeWars import views

app_name='CodeWars'

urlpatterns=[
    url(r'CodeWars/title$',views.title,name="title"),
    url(r'CodeWars/(?P<Title>[\f\w-]+)/$',views.description,name="description")
]