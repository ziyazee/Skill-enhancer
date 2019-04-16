from django import forms


from .models import *


class PostForm(forms.ModelForm):
    class Meta:   
        
        model = Aptitud
        fields = ('userName','topicName','topicDescription',)

class SubjectForm(forms.ModelForm):
    class Meta:   
        
        model = Subject
        fields = ('userName','subjectName','topicHeading','topicDescription',)

class InterviewForm(forms.ModelForm):
    class Meta:   
        
        model = InterviewExperiences
        fields = ('userName','companyName','companyExperience',)

class CodingForm(forms.ModelForm):
    class Meta:   
        
        model = popularCodingProblem
        fields = ('userName','topicHeading','topicDescription',)


