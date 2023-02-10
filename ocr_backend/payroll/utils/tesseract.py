from PIL import Image
from pytesseract import Output
import pytesseract
import numpy as np
import cv2
import os
from dotenv import load_dotenv

load_dotenv()

# pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT')

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

  norm_img = np.zeros((img.shape[0], img.shape[1]))
  img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
  img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
  img = cv2.GaussianBlur(img, (1, 1), 0)
  img = img.astype(np.uint8)
  
  text = pytesseract.image_to_string(img,config=myconfig)

  return text

  # FILENAME = 'apple.jpeg'
  # myconfig = r"--psm 3"
  # img = cv2.imread(FILENAME)
  # height, width, _ = img.shape
  # data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
  # amount_boxes = len(data['text'])
  # for i in range(amount_boxes):
  #   if float(data['conf'][i]) > 80:
  #     (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
  #     img = cv2.rectangle(img, (x, y), (x+width, y+height), (0,255,0), 2)
  #     img = cv2.putText(img, data['text'][i], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,200), 2, cv2.LINE_AA)
  #     print(data['text'][i])

  # img = cv2.resize(img, (1000,1000), interpolation=cv2.INTER_AREA)
  # cv2.imshow("img", img)
  # cv2.waitKey(0)

  