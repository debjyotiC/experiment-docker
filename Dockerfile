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

# Remove the default Nginx configuration file
RUN rm /etc/nginx/sites-available/default

# Copy the custom Nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port that the app will run on
EXPOSE 5000

# Define the command to run the application and start Nginx
CMD ["bash", "-c", "service nginx start && python server.py"]
