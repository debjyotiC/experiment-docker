# Flask App with Docker and Nginx

This repository provides a simple example of a Flask web application deployed using Docker and managed by Nginx as a reverse proxy.

## Prerequisites

Make sure you have the following installed on your machine:

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-docker-nginx.git
   cd flask-docker-nginx

2. Build the Docker image using the following command
    ```bash
    docker build -t server .
   
3. Run the Docker container using the following command
    ```bash
    docker run -p 5000:5000 server
