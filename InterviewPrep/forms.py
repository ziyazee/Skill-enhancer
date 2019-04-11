from django import forms


from .models import *


class PostForm(forms.ModelForm):
    class Meta:   
        
        model = Aptitude
        fields = ('topicName','topicDescription',)

class SubjectForm(forms.ModelForm):
    class Meta:   
        
        model = Subjects
        fields = ('subjectName','topicHeading','topicDescription',)

class InterviewForm(forms.ModelForm):
    class Meta:   
        
        model = InterviewExperience
        fields = ('companyName','companyExperience',)

class CodingForm(forms.ModelForm):
    class Meta:   
        
        model = popularCodingProblems
        fields = ('topicHeading','topicDescription',)


