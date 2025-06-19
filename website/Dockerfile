# Use the official Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the project
COPY . .

RUN apt-get update
RUN apt-get upgrade -y

# Install build tools (gcc, python3-dev) and other dependencies
RUN apt-get install -y \
    gcc \
    python3-dev \
    build-essential \
    libssl-dev \
    libfreetype6-dev \
    zlib1g-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    libwebp-dev \
    tcl8.6-dev tk8.6-dev \
    python3-tk \
    && apt-get clean
    
# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --trusted-host https://mirror-pypi.runflare.com -i https://mirror-pypi.runflare.com/simple/

# Expose the port the app runs on
EXPOSE 8000
