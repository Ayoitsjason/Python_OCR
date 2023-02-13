from django.test import Client
import io
from PIL import Image


def create_dummy_image():
    # Create an in-memory binary stream
    image_binary_data = io.BytesIO()
    
    # Create a dummy image and save it to the binary stream
    image = Image.new('RGB', (100, 100), 'white')
    image.save(image_binary_data, 'JPEG')
    
    # Reset the binary stream's position so it can be read from the beginning
    image_binary_data.seek(0)
    
    return image_binary_data

# =============== Scan Functions =================
def test_scan_post_success():
    client = Client()
    with create_dummy_image() as image_binary_data:
        response = client.post('http://127.0.0.1:8000/payroll/scan', {'format': 'row text', 'file': image_binary_data})
        assert response.status_code == 200

def test_scan_post_empty_file():
    client = Client()
    response = client.post('http://127.0.0.1:8000/payroll/scan', {'format': 'row text'})
    assert response.status_code == 400
    assert response.content == b'Unable to scan'

def test_scan_not_found():
    client = Client()
    response = client.get('http://127.0.0.1:8000/payroll/scan')
    assert response.status_code == 404
    assert response.content == b'The requested resource could not be found.'