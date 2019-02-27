
from django.conf.urls import url
from InterviewPrep import views

app_name='InterviewPrep'

urlpatterns=[
    url(r'InterviewPrep/index$',views.indexip,name="index"),
    url(r'InterviewPrep/mail$',views.mail,name="mail"),

]