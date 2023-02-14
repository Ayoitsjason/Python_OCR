# Python_OCR
Application provides a user-friendly interface for uploading images, which are then scanned and processed to extract any readable text.

Link to Project: https://ocr-frontend.onrender.com

![ocr_snapshot](https://user-images.githubusercontent.com/11216742/217987191-1cdc2b6a-8129-4345-8962-e77d13b0102a.jpg)

# How It's Made:

**Front End**
Tech used: React and Bootstrap

**Back End**
Tech used: Python, Django, and Docker

Python OCR was constructed utilizing React, Python, and Django to create a platform for users to upload images and extract text which is then temporarily stored on the client side.

On the backend, I utilized the Django web framework and the Gunicorn web server. I leveraged Django logging to create logs, and used OpenCV for image processing. To extract embedded text, I utilized pytesseract, and for optical character recognition, we employed Tesseract.

The front-end was designed using React and React-Bootstrap for styling purposes. The user interface allows for multiple ways to scan readable text from uploaded images.

For DevOps, the front-end is hosted on Render and has scripts in place for automatic building and deployment upon every Git push to the main branch. The backend has been Dockerized and is hosted on Railway, where it is built and run after every Git push to the main branch. Unit tests were written to test API endpoints, application functionality, and conduct speed benchmarking. The backend is tested after every Git push to the development branch prior to merging with the main branch.

# Optimizations
1. Images are pre-processed using image thresholding and noise reduction to obtain more accurate text extractions.
2. The backend CPU has been upgraded to improve optical character recognition speeds.
3. Continuous integration and continuous deployment have been implemented to enhance code quality, development efficiency, and deployment time.

# Lessons Learned:
1. Keep things modular and scalable: Building a full-stack application involves working with multiple technologies, frameworks, and libraries. To keep the application maintainable and scalable, it's important to keep the components modular and loosely coupled. This makes it easier to modify and add new features as the application evolves.
2. Automated testing is critical: With so many moving parts involved in a full-stack application, it's essential to have automated tests in place to ensure that changes or updates don't introduce new issues. Pytest was a valuable tool in this regard, allowing me to test different parts of the application in an efficient and organized manner.
3. Debugging can be challenging: Working with a complex stack of technologies can make debugging issues more challenging, particularly when different technologies or frameworks are interacting with each other. It's important to have a solid understanding of each component and its role in the application, as well as tools for monitoring and debugging issues as they arise.
4. Patience and perseverance are key: Building a full-stack application with complex functionality like OCR can be challenging, and it's important to be patient and persistent when working through issues or tackling difficult problems. Breaking things down into smaller, more manageable tasks and maintaining a positive attitude can help keep the project on track and moving forward.

Copyright (c) 2023 Jason Le
