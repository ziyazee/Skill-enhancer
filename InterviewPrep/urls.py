
from django.conf.urls import url
from InterviewPrep import views

app_name='InterviewPrep'

urlpatterns=[
    url(r'InterviewPrep/index$',views.indexip,name="indexip"),
    
    url(r'InterviewPrep/subjectCatgories/$',views.subjectCatgories,name="subjectCatgories"),
    url(r'InterviewPrep/topicName/(?P<subjectName>[\f\w-]+)/$',views.topicName,name="topicName"),

    url(r'InterviewPrep/codingTopic/$',views.codingTopic,name="codingTopic"),
    url(r'InterviewPrep/topicDescription/(?P<topicHeading>[\f\w-]+)/$',views.codingDescription,name="codingDescription"),
    
    url(r'InterviewPrep/aptitudeTopic/$',views.aptitudeTopic,name="aptitudeTopic"),
    url(r'InterviewPrep/aptitudeDescription/(?P<topicName>[\f\w-]+)/$',views.aptitudeDescription,name="aptitudeDescription"),
    
    url(r'InterviewPrep/companyName/$',views.interviewTopic,name="interviewTopic"),
    url(r'InterviewPrep/companyExperience/(?P<companyName>[\f\w-]+)/$',views.companyExperience,name="companyExperience"),



]