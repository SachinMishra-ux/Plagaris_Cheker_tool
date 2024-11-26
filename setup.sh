#!/bin/bash
pip install rapidocr-onnxruntime

# Install Google Chrome
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt-get -f install -y

# Download the most stable version of Chromedriver
CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/linux64/chromedriver-linux64.zip"
echo "Downloading Chromedriver from: $CHROMEDRIVER_URL"

# Download Chromedriver
wget -q -N "$CHROMEDRIVER_URL" -O chromedriver-linux64.zip

# Check if the download was successful
if [ -f "chromedriver-linux64.zip" ]; then
    # Unzip Chromedriver to project root
    unzip -o chromedriver-linux64.zip -d .
    chmod +x chromedriver
    echo "Chromedriver installed successfully in project root."
else
    echo "Failed to download Chromedriver. Exiting."
    exit 1
fi

# Clean up the zip file
rm chromedriver-linux64.zip

# Remove the LICENSE.chromedriver file
rm -f LICENSE.chromedriver

# Clean up unnecessary files
rm google-chrome-stable_current_amd64.deb
