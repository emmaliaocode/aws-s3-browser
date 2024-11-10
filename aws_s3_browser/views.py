import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from djangoS3Browser.s3_browser.operations import *

"fetch the directories within the selected folder"


def index(request):
    return render(request, 'index.html')
