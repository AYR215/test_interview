import shutil
from os import mkdir

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from words.forms import DocumentForm
from words.models import handle_uploaded_file

def upload_file(request):
    shutil.rmtree('C:/Users/ayr21/PycharmProjects/test_interview/counter/media')
    mkdir('C:/Users/ayr21/PycharmProjects/test_interview/counter/media')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/')
            return render(request, 'success.html', {'count': (handle_uploaded_file(request.FILES['file'])[0]), 'wormcount': (handle_uploaded_file(request.FILES['file'])[1])})
    else:
        form = DocumentForm()

    return render(request, 'file_upload.html', {'form': form})
