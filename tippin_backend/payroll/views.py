from django.http.response import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from payroll.utils import tesseract 

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
      text = tesseract.imageOCR(file,data)
      logger.info('Finished scanning image')
      return JsonResponse(text, safe=False)
    except Exception as e:
        logger.exception(e)
        return JsonResponse(e, safe=False)
  elif request.method == 'GET':
    return JsonResponse("success", safe=False)
  else:  
    return HttpResponseBadRequest("Unable to post")

# {
#     "status": <HTTP status code>,
#     "data": {
#         // data payload, if applicable
#     },
#     "error": {
#         // error information, if applicable
#     }
# }