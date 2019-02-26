
from django.conf.urls import url
from MainBoard import views

app_name='MainBoard'

urlpatterns=[
    url(r'^$',views.login_view,name="login"),
    url(r'logout/$',views.logout_view,name="logout"),
    url(r'tk/$',views.tk,name="tk"),
    url(r'indi/$',views.indi,name="indi"),

]