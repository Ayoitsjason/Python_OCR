from django.http.response import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import tesseract 

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@csrf_exempt
def scan(request):
  if request.method == 'POST':
    file = request.FILES.get('file')
    data = request.POST.get('format')
    logger.info('Start scanning image')
    try:
      if file is None:
        raise ValueError("Empty File")
      text = tesseract.imageOCR(file,data)
      logger.info('Finished scanning image')
      return JsonResponse(text, safe=False)
    except Exception as e:
      logger.exception(e)
      return HttpResponseBadRequest("Unable to scan")
  else:  
    return HttpResponseNotFound("The requested resource could not be found.")