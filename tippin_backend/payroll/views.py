from django.http.response import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from payroll.utils import tesseract 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def scan(request):
  if request.method == 'POST':
    file = request.FILES.get('file')
    data = request.POST.get('orientation')
    logger.info('Start scanning image')
    try:
      text = tesseract.imageOCR(file,data)
      logger.info('Finished scanning image')
      json = {{'status': 200},{"data": text },{'error': {}}}
      return JsonResponse(json, safe=False)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({'status': 500},{'data': {}},{'error': {'message': e.args[0]}})
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