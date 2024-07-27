# Use the official Python image with Alpine Linux
FROM python:3.12.4-alpine AS base

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run migrations
RUN python manage.py migrate

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Stage for running tests
FROM base AS test

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Run migrations
RUN python manage.py migrate

# Command to run tests
CMD ["python", "manage.py", "test"]