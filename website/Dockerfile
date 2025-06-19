# Use the official Python image
FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the project
COPY . .

RUN echo "https://mirror.arvancloud.ir/alpine/v3.22/main" > /etc/apk/repositories
RUN apk add build-base

# Install dependencies
RUN pip install --upgrade pip --trusted-host https://mirror-pypi.runflare.com -i https://mirror-pypi.runflare.com/simple/
RUN pip install -r requirements.txt --trusted-host https://mirror-pypi.runflare.com -i https://mirror-pypi.runflare.com/simple/

# Expose the port the app runs on
EXPOSE 8000
