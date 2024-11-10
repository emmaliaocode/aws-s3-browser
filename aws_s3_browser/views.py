from django.shortcuts import render

from djangoS3Browser.s3_browser.operations import *

"fetch the directories within the selected folder"


def index(request):
    return render(request, 'index.html')
