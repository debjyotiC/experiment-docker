# Use the official Python image as a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Expose the port that the app will run on
EXPOSE 80

# Define the command to run the application
CMD ["bash", "-c", "nginx -g 'daemon off;' & python app.py"]
