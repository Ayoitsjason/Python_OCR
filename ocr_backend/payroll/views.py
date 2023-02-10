from django.http.response import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from payroll.utils import tesseract 
# import timeit

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def scan(request):
  if request.method == 'POST':
    file = request.FILES.get('file')
    data = request.POST.get('format')
    logger.info('Start scanning image')
    try:
      if file is None:
        raise ValueError("Empty File")
      # time = timeit.timeit(lambda: tesseract.imageOCR(file,data), number=1)
      # print("Time taken: ", time, "seconds")
      text = tesseract.imageOCR(file,data)
      logger.info('Finished scanning image')
      return JsonResponse(text, safe=False)
    except Exception as e:
      logger.exception(e)
      return HttpResponseBadRequest("Unable to scan")
  elif request.method == 'GET':
    return JsonResponse("success", safe=False)
  else:  
    return HttpResponseNotFound("Not Found")