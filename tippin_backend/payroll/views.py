from django.shortcuts import render
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def scan(request):
  if request.method == 'POST':
    return JsonResponse("success", safe=False)
  elif request.method == 'GET':
    return JsonResponse("success", safe=False)
  else:  
    return HttpResponseBadRequest("Unable to post")

    