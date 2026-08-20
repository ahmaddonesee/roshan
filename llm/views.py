from django.shortcuts import render,redirect
from .models import UploadFile,Comment
from .forms import UploadFileForm,CommentForm
from django.contrib.auth.models import User

def upload_file(request):
    form=UploadFileForm()
    if request.method=="POST":
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.author = request.user
            form2.save()
            return redirect('llm:uploadfile')
    else:
        form=UploadFileForm()
        context={
            'form':form,
        }
    return render(request,'uploads/upload.html',context)

def edite_file(request):
    return render(request,'uploads/edit.html')


def delete_file(request):
    pass
