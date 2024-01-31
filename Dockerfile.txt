# Use the official Python image as a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app will run on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "server.py"]
