import pytesseract
import numpy as np
import cv2


def imageOCR(file,format):
  myconfig = r"--psm 3"
  if format == 'Column Text':
    myconfig = r"--psm 4"
  elif format == 'Block Text':
    myconfig = r"--psm 6"
  elif format == 'Single Text Line':
    myconfig = r"--psm 7"
  elif format == 'Single Word':
    myconfig = r"--psm 8"

  image_data = np.asarray(bytearray(file.read()), dtype=np.uint8)
  img = cv2.imdecode(image_data, cv2.IMREAD_UNCHANGED)
  
  img = reduceImgSize(img)
  norm_img = np.zeros((img.shape[0], img.shape[1]))
  img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
  img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
  img = cv2.GaussianBlur(img, (1, 1), 0)
  img = img.astype(np.uint8)
  
  text = pytesseract.image_to_string(img,config=myconfig)

  return text

def reduceImgSize(img):
  height, width = img.shape[:2]
  aspect_ratio = height / width
  new_width = width
  if width > 800:
    new_width = int(width * .50)
  new_height = int(new_width * aspect_ratio)
  img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
  return img

  