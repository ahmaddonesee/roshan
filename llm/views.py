from django.shortcuts import render,redirect
from .models import UploadFile,Comment
from .forms import UploadFileForm,CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def upload_file(request,id=None):
    form=UploadFileForm()
    uploadfiles=UploadFile.objects.all()
    if request.method=="POST":
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.author = request.user
            form2.save()
            # print(type(form.cleaned_data['file']))
            # file=form.cleaned_data['file']
            # with file.open(mode='r') as file:
            #     content = file.read()
            #     print(content)
            #     print(22)
            #     file.close()
            # form2=form.save(commit=False)
            # form2.author = request.user
            # form2.save()
            return redirect('llm:upload_file')
        else:
            return HttpResponse("invalid import")
    else:
        uploadfiles=UploadFile.objects.all()
        form=UploadFileForm()
        context={
            'form':form,
            'uploadfiles':uploadfiles,
            
        }
        return render(request,'uploads/upload.html',context)

def edite_file(request,id):
    uploadfile=UploadFile.objects.get(id=id)
    form=UploadFileForm()
    if request.method=="POST":
        form=UploadFileForm(request.POST,request.FILES,instance=uploadfile)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.author = request.user
            form2.save()
            # updated_f = form.save(commit=False)
            # updated_f.author = uploadfile.author
            # updated_f.file = form.cleaned_data["file"]
            # name=form.cleaned_data["name"]
            # text=form.cleaned_data["text"]
            # file=form.cleaned_data["file"]
            # newbupload=UploadFile(name=name,text=text,file=file,author=uploadfile.author)
            # newbupload.save()
            # uploadfile.delete()
            # return redirect(reverse("blog:blog_detail",kwargs={'id':newblog.id}))
            return redirect("llm:upload_file")
        else:
            return HttpResponse("error")
            
    else:
        form=UploadFileForm()
        uploadfile=UploadFile.objects.get(id=id)
        context={
            "form":form,
            'uploadfile':uploadfile,
            # 'content':content
        }
        return render(request,"uploads/edite.html",context)


def delete_file(request,id):
    uploadfile=UploadFile.objects.get(id=id)
    user=User.objects.get(username=request.user.username)
    if user==uploadfile.author or request.user.is_superuser :
        uploadfile.delete()
        return redirect('llm:upload_file')



def read_file(request, id):
    uploadfile = UploadFile.objects.get(id=id)

    with uploadfile.file.open(mode='r') as file:
        content = file.read()
        # print(999999999999999999999999999999999999)
        # print(content)
        # print(999999999999999999999999999999999)
        # content.close()

    return render(
        request,
        'uploads/read.html',
        {
            'uploadfile': uploadfile,
            'content': content,
        }
    )