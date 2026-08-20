from django import forms
from .models import UploadFile,Comment


# make form for uploadfie model
class UploadFileForm(forms.ModelForm):
    class Meta:
        model=UploadFile
        fields=['name','text','file']
        
# make form for Comment model   
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']