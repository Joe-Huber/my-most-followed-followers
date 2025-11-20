# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies required for headless Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    --no-install-recommends

# Install Google Chrome using the modern, secure method
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Install ChromeDriver
# This command finds the latest stable ChromeDriver version for the installed Chrome
RUN CHROME_DRIVER_VERSION=$(wget -q -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(google-chrome --version | cut -d' ' -f3 | cut -d'.' -f1)") \
    && wget -q --continue -P /usr/local/bin "https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin \
    && rm /usr/local/bin/chromedriver_linux64.zip

# Copy the application code into the container
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint for the container
ENTRYPOINT ["python", "/app/entrypoint.py"]
