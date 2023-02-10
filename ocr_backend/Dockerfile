# syntax = docker/dockerfile:1.2

# Use an official Python runtime as the base image
FROM python:3.8

# Install Tesseract
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 tesseract-ocr

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files to the container
COPY . /app

# Set environment variables
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV RENDER_EXTERNAL_HOSTNAME=$RENDER_EXTERNAL_HOSTNAME

# Record which port you will expose
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "ocr_backend.wsgi:application"]