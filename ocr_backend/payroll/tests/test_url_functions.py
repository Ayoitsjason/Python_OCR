# from django.test import Client
# from ..views import scan
# import json

# # =============== Scan Functions =================
# def test_scan_post_success():
#     client = Client()
#     request = client.post('http://127.0.0.1:8000/payroll/scan', {'format': 'text'}, content_type='multipart/form-data')
#     request.FILES = {'file': None}
#     response = scan(request)
#     assert response.status_code == 200

# def test_scan_post_empty_file():
#     client = Client()
#     request = client.post('http://127.0.0.1:8000/payroll/scan', {'format': 'text'}, content_type='multipart/form-data')
#     request.FILES = {}
#     response = scan(request)
#     assert response.status_code == 400
#     assert json.loads(response.content) == 'Unable to scan'

# def test_scan_not_found():
#     client = Client()
#     request = client.get('http://127.0.0.1:8000/payroll/scan')
#     response = scan(request)
#     assert response.status_code == 404
#     assert json.loads(response.content) == 'Only Post Request Allowed'