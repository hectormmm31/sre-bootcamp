# syntax=docker/dockerfile:1

# Image base
FROM python:3-alpine

# Set the working directory
WORKDIR /app

# Set enviroment variables
ENV FLASK_APP=api.py
ENV FLASK_DEBUG=1

# Expose the applications´s port
EXPOSE 8000

# Install dependencies for mysql connection
RUN apk add --no-cache mariadb-dev build-base

# Copy requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Mount Volume
#VOLUME [ "/app" ]

# Copy Code
#COPY . .

# Run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]