# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install the app's dependencies
RUN pip install Flask

# Expose port 80 to allow traffic to the web server
EXPOSE 80

# The command to run when the container starts
CMD ["python", "app.py"]