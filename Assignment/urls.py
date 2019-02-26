
from django.conf.urls import url
from Assignment import views

app_name='Assignment'

urlpatterns=[
    url(r'logout/$',views.logout_view,name="logout"),
    url(r'Assignment/index/$',views.index,name="index"),
    url(r'Assigment/posts/$',views.posted,name="post"),
    url(r'Assignment/assignmentList/(?P<subjects>[\f\w-]+)/$',views.assignmentList,name='assignmentList'),
    url(r'Assignment/uploadsInfo/(?P<upload>[\f\w-]+)/$',views.uploadInfo,name='uploadInfo'),
    url(r'Assignment/delete/(?P<assignmentName>[\f\w-]+)/$',views.deleteMyAssignment,name='delete'),

]

