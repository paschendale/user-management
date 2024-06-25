# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
